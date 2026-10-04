#!/usr/bin/env python3
"""Uç noktaları bir ortamda (sandbox / production) dener ve sonucu spec/test_status.json'a yazar.

    python scripts/check_endpoints.py                       # sandbox
    python scripts/check_endpoints.py --environment production
    python scripts/check_endpoints.py --only fx.fx_currency_rates

Güvenlik kuralları:

* Yalnızca aşağıdaki ``READ_ONLY`` listesinde **elle** onaylanmış, veri okuyan uç noktalar
  çağrılır. Listede olmayan hiçbir uç noktaya istek atılmaz; para hareketi, ödeme, başvuru,
  kayıt oluşturma/iptal, bildirim ya da SMS gönderen uç noktalar bu yüzden hiç çağrılmaz ve
  "test edilmedi" olarak kalır. Yeni bir uç nokta, gözden geçirilip listeye eklenene kadar
  çağrılmaz.
* Müşteri girişi (authorization code) isteyen uç noktalar çağrılmaz.
* Yanıt içerikleri dosyaya yazılmaz; yalnızca durum kodu, kayıt sayısı ve maskelenmiş hata
  mesajı saklanır.
* İstekler aralıklı gönderilir (sunucu hızlı istekleri IP bazında engelliyor).

Betik yalnızca kendi çağırdığı uç noktaların kaydını günceller; çağırmadığı bir uç noktanın
elle girilmiş kaydına dokunmaz (ör. müşteri girişiyle elle yapılan bir test).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from typing import Any

from kuveytturk_api import (
    APIError,
    AuthenticationError,
    KuveytTurk,
    KuveytTurkError,
    TransportError,
)

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "spec" / "endpoints.json"
STATUS = ROOT / "spec" / "test_status.json"
SECTIONS = {"sandbox": "sandbox", "production": "canli"}

TESTED = "test edildi"
PARTIAL = "kısmen test edildi"
NOT_TESTED = "test edilmedi"

# Elle gözden geçirilmiş, yalnızca veri okuyan uç noktalar (kaynak.metot). Bir uç noktayı
# buraya eklemeden önce dokümanını okuyun: hiçbir koşulda para hareketi, ödeme, kayıt
# oluşturma/değiştirme ya da bildirim/SMS gönderme yapmamalı.
READ_ONLY = frozenset(
    {
        # hesaplar
        "accounts.account_list_v3",
        "accounts.account_list_with_suffix_v3",
        "accounts.account_transactions_v3",
        "accounts.account_transactions_v4_detail",
        "accounts.receipt_v3",
        "accounts.pdf_receipt_v3",
        "accounts.account_activity_list",
        # kartlar
        "cards.credit_card_list_v3",
        "cards.credit_card_transactions_list_v3",
        # döviz ve hazine (kur sorguları)
        "fx.fx_currency_list",
        "fx.fx_currency_rates",
        "treasury.fx_and_precious_metal_rates",
        "treasury.precious_metal_rates",
        # bilgi servisleri
        "information.bank_list",
        "information.bank_branch_list",
        "information.kuveyt_turk_atm_list",
        "information.kuveyt_turk_branch_list",
        "information.kuveyt_turk_xtm_list",
        "information.loan_finance_calculation_parameter",
        "information.iban_validation_utility",
        "information.get_class_info",
        "information.collection_list",
        "information.calculate_profit_share_rate",
        # transfer sorguları (transfer yapmaz)
        "transfers.customer_iban_info_for_money_transfer",
        "transfers.money_transfer_state",
        "transfers.transaction_validation_list",
        "transfers.investment_account_activities_report",
        # toplu transfer için hesap doğrulama sorguları
        "payments.account_validation_by_account_number_for_group_money_transfer",
        "payments.account_validation_by_iban_for_group_money_transfer",
        "payments.account_validation_by_iban_for_group_money_transfer_v2",
        "payments.kt_bank_error_message_list",
        "payments.kuveyt_turk_branch_list_for_group_money_transfer",
        # finansman: hesaplama ve listeler
        "financing.loan_finance_calculation",
        "financing.loans_price_list",
        "financing.customer_suited_card_list",
        "financing.get_digital_channel_card_application_list_v2",
        "financing.customer_current_credit_allocation_flow_information",
        # nakit yönetimi: sorgular
        "cash_management.cheque_information_micro",
        "cash_management.digital_banking_transaction_status",
        "cash_management.school_installment_payment_system_active_registration_inquiry",
        "cash_management.supplier_financing_buyer_order_listing",
        "cash_management.supplier_financing_vendor_invoice_listing",
        "cash_management.supplier_financing_repayment_plan_calculation",
        # kredibilite sorguları
        "credibility.customer_overall_limit_values",
        "credibility.tardes_agricultural_score_inquiry",
        "credibility.taxpayer_gib_identity_information",
        # ödeme çözümleri: sorgular
        "payment_solutions.pos_merchant_number_list",
        "payment_solutions.digital_payment_query",
        "payment_solutions.pos_transaction_details_v3",
        "payment_solutions.pos_transactions_summary_v3",
        # e-ticaret: sorgular
        "ecommerce.ecommerce_get_lending_information_v1",
        "ecommerce.ecommerce_get_lending_information_v1_2",
        "ecommerce.ecommerce_monthly_payments_v1",
        "ecommerce.ecommerce_monthly_payments_v1_2",
        "ecommerce.ecommerce_pre_approved_monthly_payments_v1",
        "ecommerce.ecommerce_pre_approved_monthly_payments_v1_2",
        # diğer sorgular
        "hgs.hgs_balance_information",
        "hgs.hgs_product_information",
        "hgs.hgs_usage_transactions",
        "moneygram.money_gram_country_list",
        "moneygram.money_gram_currency_list",
        "moneygram.money_gram_query_fee",
        "support.kt_incident_activity_type_list",
        "support.kt_incident_defined_document_list",
        "support.kt_incident_product_list",
        "support.kt_incident_info",
        "support.kt_incident_optional_field_list",
        "support.kt_incident_neova_info",
        "support.kt_incident_neova_list",
        "sms_otp.pr_get_fast_result",
        "donations.donation_list_for_organization",
        "your_banking.your_banking_account_application_status_query",
        "other.fraud_notifications_exists",
        "other.get_fraud_notifications_last_day",
        "other.get_process_design_xml_by_business_process_id",
        "other.calculate_welcome_participation_account_profit_share",
        "other.credi_tech_intelligence_inquiry_by_credit_allocation_status",
        "architecht.customer_consent_list",
        "vpos.get_seller_order_details",
        "vpos.order_detail_with_payment_id",
        # Müşteri girişi isteyen okuma uç noktaları: betik bunları çağırmaz ("müşteri girişi
        # gerekiyor" yazar); müşteri girişiyle elle test edilince kayıt elle güncellenir.
        "tpp_accounts.account_list_v2",
        "tpp_accounts.account_list_with_suffix_v2",
        "tpp_accounts.account_transactions_v2",
        "tpp_accounts.receipt_v1",
        "tpp_accounts.receipt_v2",
        "financing.loan_finance_info",
        "financing.loan_finance_installments",
        "financing.loan_finance_list",
        "payments.invoice_company_list",
        "payments.check_money_transfers_status_from_kt_bank_to_kuveyt_turk",
        "donations.account_transactions_for_the_organization",
        "donations.campaign_list_for_organization",
        "donations.external_payments_list",
        "moneygram.money_gram_query_reference",
        "payment_solutions.pos_transaction_details_for_tpp_v2",
        "payment_solutions.pos_transactions_summary_for_tpp_v2",
        "payment_solutions.virtual_pos_end_day_all_list",
        "payment_solutions.virtual_pos_order_filter",
    }
)

_MASKS = (
    (re.compile(r"\bTR\d{2}[0-9 ]{10,30}\d\b"), "TR**…"),  # IBAN
    (re.compile(r"\b\d{6,}\b"), "<sayı>"),  # hesap/kart/müşteri numarası benzeri uzun sayılar
)


def mask(text: str, limit: int = 160) -> str:
    for pattern, replacement in _MASKS:
        text = pattern.sub(replacement, text)
    text = " ".join(text.split())
    return text[:limit] + ("…" if len(text) > limit else "")


def key_of(endpoint: dict[str, Any]) -> str:
    return f"{endpoint['resource']}.{endpoint['name']}"


def summarize_value(data: Any) -> str:
    """Yanıtın içeriğini değil şeklini özetler (kayıt sayısı)."""
    value = data.get("value", data) if isinstance(data, dict) else data
    if isinstance(value, list):
        return f"{len(value)} kayıt"
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, list):
                return f"{key}: {len(item)} kayıt"
        return "nesne"
    return "boş" if value in (None, "") else "değer"


def discover_context(kt: KuveytTurk, delay: float) -> dict[str, Any]:
    """Gerçek değer gerektiren parametreler için uygulamanın kendi hesaplarından değer bulur.

    Değerler yalnızca bellekte tutulur, hiçbir yere yazılmaz.
    """
    context: dict[str, Any] = {}
    try:
        accounts = kt.accounts.account_list_v3()["accountList"] or []
    except (KuveytTurkError, KeyError, TypeError):
        return context
    if accounts:
        context["suffix"] = accounts[0].get("suffix")
        context["iban"] = accounts[0].get("iban")
    # Dekont gibi uçlar için bir hareket referansı: hareketi olan ilk hesaptan (en çok 5 deneme).
    for account in accounts[:5]:
        time.sleep(delay)
        try:
            activities = kt.accounts.account_transactions_v3(suffix=account["suffix"], item_count=1)
        except (KuveytTurkError, KeyError):
            continue
        rows = activities.get("accountActivities") or []
        if rows and rows[0].get("transactionReference"):
            context["transactionreference"] = rows[0]["transactionReference"]
            break
    return context


def build_kwargs(endpoint: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    """Zorunlu parametrelerden değeri bilinenleri (ek no, IBAN) doldurur; diğerleri gönderilmez."""
    return {
        param["name"]: context[param["wire"].lower()]
        for group in ("path_params", "query_params", "body_params")
        for param in endpoint[group]
        if param["required"] and context.get(param["wire"].lower()) is not None
    }


def missing_path_params(endpoint: dict[str, Any], kwargs: dict[str, Any]) -> list[str]:
    return [p["wire"] for p in endpoint["path_params"] if p["required"] and p["name"] not in kwargs]


def record(durum: str, sonuc: str, ayrinti: str = "", http: int | None = None) -> dict[str, Any]:
    entry: dict[str, Any] = {"durum": durum, "sonuc": sonuc, "tarih": dt.date.today().isoformat()}
    if http is not None:
        entry["http"] = http
    if ayrinti:
        entry["ayrinti"] = ayrinti
    return entry


def raw_request(kt: KuveytTurk, endpoint: dict[str, Any], kwargs: dict[str, Any]) -> Any:
    """Hazır metodu atlayıp isteği yalnızca verilen parametrelerle gönderir."""

    def pick(group: str) -> dict[str, Any]:
        return {p["wire"]: kwargs[p["name"]] for p in endpoint[group] if p["name"] in kwargs}

    body: Any = None
    if endpoint["method"] in ("POST", "PUT", "PATCH"):
        body = pick("body_params")
        for key in reversed(endpoint["body_wrap"]):
            body = {key: body}
    return kt.request(
        endpoint["method"],
        endpoint["path"],
        scope=endpoint["scope"],
        flow=endpoint["flow"],
        path_params=pick("path_params") or None,
        query=pick("query_params"),
        body=body,
    )


def check(kt: KuveytTurk, endpoint: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    kwargs = build_kwargs(endpoint, context)
    missing = missing_path_params(endpoint, kwargs)
    if missing:
        return record(
            NOT_TESTED, "parametre değeri bilinmiyor", f"yol parametresi: {', '.join(missing)}"
        )
    required = [
        p
        for g in ("path_params", "query_params", "body_params")
        for p in endpoint[g]
        if p["required"]
    ]
    try:
        if all(p["name"] in kwargs for p in required):
            # Bütün zorunlu değerler biliniyor: kütüphanenin hazır metodu çağrılır.
            response = getattr(getattr(kt, endpoint["resource"]), endpoint["name"])(**kwargs)
        else:
            # Bazı zorunlu değerler bilinmiyor: istek bilinenlerle doğrudan atılır; API eksik
            # alanları doğrulama hatası olarak bildirir (uç noktanın varlığı ve yetki görülür).
            response = raw_request(kt, endpoint, kwargs)
    except AuthenticationError as exc:
        if exc.error == "invalid_scope":
            return record(
                NOT_TESTED, "uygulamanın kapsam yetkisi yok", f"kapsam: {endpoint['scope']}"
            )
        return record(NOT_TESTED, "token alınamadı", mask(str(exc)))
    except APIError as exc:
        detail = mask(exc.error_message or str(exc.body or exc))
        if exc.status_code == 404 and "path not found" in detail.lower():
            return record(TESTED, "bu ortamda yok (404)", detail, exc.status_code)
        if exc.status_code == 403:
            return record(NOT_TESTED, "uygulamanın kapsam yetkisi yok", detail, exc.status_code)
        if exc.status_code == 401:
            return record(NOT_TESTED, "yetkilendirme reddedildi", detail, exc.status_code)
        if exc.status_code >= 500:
            return record(TESTED, "sunucu hatası", detail, exc.status_code)
        # 400 ya da success: false -> uç nokta var ve yetki tamam; eksik/örnek parametre yüzünden
        # gerçek bir yanıt alınamadı.
        return record(PARTIAL, "erişilebilir, parametre/iş kuralı hatası", detail, exc.status_code)
    except TransportError as exc:
        return record(NOT_TESTED, "bağlantı hatası", mask(str(exc)))
    sent = ", ".join(sorted(kwargs)) or "parametresiz"
    return record(
        TESTED, "çalışıyor", f"{summarize_value(response.data)} ({sent})", response.status_code
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--environment", default="sandbox", choices=sorted(SECTIONS))
    parser.add_argument("--delay", type=float, default=4.0, help="istekler arası bekleme (saniye)")
    parser.add_argument("--only", action="append", help="yalnızca bu uç nokta(lar) (kaynak.metot)")
    parser.add_argument("--env-file", default=str(ROOT / ".env"))
    args = parser.parse_args()

    endpoints = json.loads(SPEC.read_text(encoding="utf-8"))
    status = json.loads(STATUS.read_text(encoding="utf-8")) if STATUS.exists() else {}
    entries: dict[str, Any] = status.setdefault("endpoints", {})
    section = SECTIONS[args.environment]

    kt = KuveytTurk.from_env(args.env_file, environment=args.environment, max_retries=0)
    context = discover_context(kt, args.delay)
    time.sleep(args.delay)

    selected = [e for e in endpoints if not args.only or key_of(e) in args.only]
    counts: dict[str, int] = {}
    for index, endpoint in enumerate(selected, 1):
        key = key_of(endpoint)
        entry = entries.setdefault(endpoint["id"], {})
        entry["metot"] = key
        entry["istek"] = f"{endpoint['method']} {endpoint['path']}"
        called = False
        if key not in READ_ONLY:
            result = record(NOT_TESTED, "işlem yapan uç nokta; otomatik test edilmez")
        elif endpoint["flow"] == "authorization_code":
            result = record(NOT_TESTED, "müşteri girişi gerekiyor")
        else:
            try:
                result = check(kt, endpoint, context)
            except Exception as exc:  # bir uç noktadaki beklenmeyen hata diğerlerini durdurmasın
                result = record(NOT_TESTED, "betik hatası", mask(f"{type(exc).__name__}: {exc}"))
            called = True
        # Çağrılmayan uç noktada elle girilmiş bir kayıt varsa onu koru.
        if called or section not in entry:
            entry[section] = result
        entry.setdefault("sandbox", {"durum": NOT_TESTED, "sonuc": "henüz denenmedi"})
        entry.setdefault("canli", {"durum": NOT_TESTED, "sonuc": "henüz denenmedi"})
        counts[entry[section]["durum"]] = counts.get(entry[section]["durum"], 0) + 1
        mark = "→" if called else " "
        print(
            f"[{index:3}/{len(selected)}] {mark} {key:70} {entry[section]['durum']}: {entry[section]['sonuc']}"
        )
        if called:
            time.sleep(args.delay)

    known = {e["id"] for e in endpoints}
    status["endpoints"] = {
        k: entries[k] for k in sorted(entries, key=lambda k: entries[k]["metot"]) if k in known
    }
    status["_aciklama"] = (
        "Uç noktaların sandbox ve canlı ortamda test durumu. scripts/check_endpoints.py yazar; "
        "elle de düzenlenebilir (durum: 'test edildi' | 'kısmen test edildi' | 'test edilmedi'). "
        "Değiştirdikten sonra scripts/generate.py ile doküman sayfalarını yeniden üretin."
    )
    STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\n{args.environment}: " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
