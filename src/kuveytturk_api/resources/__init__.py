"""Uç nokta grupları ve istemcilere eklenen kaynak özellikleri.

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from ._resource import AsyncResource, Resource, ResourceHost
from .accounts import Accounts, AsyncAccounts
from .architecht import Architecht, AsyncArchitecht
from .cards import AsyncCards, Cards
from .cash_management import AsyncCashManagement, CashManagement
from .credibility import AsyncCredibility, Credibility
from .donations import AsyncDonations, Donations
from .ecommerce import AsyncEcommerce, Ecommerce
from .financing import AsyncFinancing, Financing
from .fx import AsyncFx, Fx
from .hgs import AsyncHgs, Hgs
from .information import AsyncInformation, Information
from .moneygram import AsyncMoneygram, Moneygram
from .other import AsyncOther, Other
from .payment_solutions import AsyncPaymentSolutions, PaymentSolutions
from .payments import AsyncPayments, Payments
from .sgk import AsyncSgk, Sgk
from .sms_otp import AsyncSmsOtp, SmsOtp
from .support import AsyncSupport, Support
from .tpp_accounts import AsyncTppAccounts, TppAccounts
from .transfers import AsyncTransfers, Transfers
from .treasury import AsyncTreasury, Treasury
from .vpos import AsyncVpos, Vpos
from .your_banking import AsyncYourBanking, YourBanking

__all__ = [
    "Accounts",
    "Architecht",
    "AsyncAccounts",
    "AsyncArchitecht",
    "AsyncCards",
    "AsyncCashManagement",
    "AsyncCredibility",
    "AsyncDonations",
    "AsyncEcommerce",
    "AsyncFinancing",
    "AsyncFx",
    "AsyncHgs",
    "AsyncInformation",
    "AsyncMoneygram",
    "AsyncOther",
    "AsyncPaymentSolutions",
    "AsyncPayments",
    "AsyncResource",
    "AsyncResourcesMixin",
    "AsyncSgk",
    "AsyncSmsOtp",
    "AsyncSupport",
    "AsyncTppAccounts",
    "AsyncTransfers",
    "AsyncTreasury",
    "AsyncVpos",
    "AsyncYourBanking",
    "Cards",
    "CashManagement",
    "Credibility",
    "Donations",
    "Ecommerce",
    "Financing",
    "Fx",
    "Hgs",
    "Information",
    "Moneygram",
    "Other",
    "PaymentSolutions",
    "Payments",
    "Resource",
    "ResourcesMixin",
    "Sgk",
    "SmsOtp",
    "Support",
    "TppAccounts",
    "Transfers",
    "Treasury",
    "Vpos",
    "YourBanking",
]


class ResourcesMixin(ResourceHost):
    """Senkron istemcinin kaynak özellikleri (``kt.accounts`` gibi)."""

    @property
    def accounts(self) -> Accounts:
        """Hesap yönetimi (kurumun kendi hesapları) (8 uç nokta)."""
        return self._resource("accounts", Accounts)

    @property
    def architecht(self) -> Architecht:
        """Architecht (3 uç nokta)."""
        return self._resource("architecht", Architecht)

    @property
    def cards(self) -> Cards:
        """Kredi kartı işlemleri (4 uç nokta)."""
        return self._resource("cards", Cards)

    @property
    def cash_management(self) -> CashManagement:
        """Nakit yönetimi (17 uç nokta)."""
        return self._resource("cash_management", CashManagement)

    @property
    def credibility(self) -> Credibility:
        """Kredibilite (5 uç nokta)."""
        return self._resource("credibility", Credibility)

    @property
    def donations(self) -> Donations:
        """Bağışlar (5 uç nokta)."""
        return self._resource("donations", Donations)

    @property
    def ecommerce(self) -> Ecommerce:
        """E-ticaret (10 uç nokta)."""
        return self._resource("ecommerce", Ecommerce)

    @property
    def financing(self) -> Financing:
        """Finansman çözümleri (16 uç nokta)."""
        return self._resource("financing", Financing)

    @property
    def fx(self) -> Fx:
        """Döviz işlemleri (5 uç nokta)."""
        return self._resource("fx", Fx)

    @property
    def hgs(self) -> Hgs:
        """HGS servisleri (3 uç nokta)."""
        return self._resource("hgs", Hgs)

    @property
    def information(self) -> Information:
        """Bilgi servisleri (şube, ATM, parametre sorguları...) (12 uç nokta)."""
        return self._resource("information", Information)

    @property
    def moneygram(self) -> Moneygram:
        """MoneyGram (6 uç nokta)."""
        return self._resource("moneygram", Moneygram)

    @property
    def other(self) -> Other:
        """Diğer (9 uç nokta)."""
        return self._resource("other", Other)

    @property
    def payment_solutions(self) -> PaymentSolutions:
        """Ödeme çözümleri (15 uç nokta)."""
        return self._resource("payment_solutions", PaymentSolutions)

    @property
    def payments(self) -> Payments:
        """Ödemeler (15 uç nokta)."""
        return self._resource("payments", Payments)

    @property
    def sgk(self) -> Sgk:
        """SGK (1 uç nokta)."""
        return self._resource("sgk", Sgk)

    @property
    def sms_otp(self) -> SmsOtp:
        """SMS / OTP (5 uç nokta)."""
        return self._resource("sms_otp", SmsOtp)

    @property
    def support(self) -> Support:
        """Destek yönetimi (14 uç nokta)."""
        return self._resource("support", Support)

    @property
    def tpp_accounts(self) -> TppAccounts:
        """Hesap yönetimi (TPP - müşteri adına) (5 uç nokta)."""
        return self._resource("tpp_accounts", TppAccounts)

    @property
    def transfers(self) -> Transfers:
        """Para transferleri (10 uç nokta)."""
        return self._resource("transfers", Transfers)

    @property
    def treasury(self) -> Treasury:
        """Hazine servisleri (kıymetli maden, kur) (5 uç nokta)."""
        return self._resource("treasury", Treasury)

    @property
    def vpos(self) -> Vpos:
        """Sanal POS (15 uç nokta)."""
        return self._resource("vpos", Vpos)

    @property
    def your_banking(self) -> YourBanking:
        """Senin Bankan (4 uç nokta)."""
        return self._resource("your_banking", YourBanking)


class AsyncResourcesMixin(ResourceHost):
    """Asenkron istemcinin kaynak özellikleri (``kt.accounts`` gibi)."""

    @property
    def accounts(self) -> AsyncAccounts:
        """Hesap yönetimi (kurumun kendi hesapları) (8 uç nokta)."""
        return self._resource("accounts", AsyncAccounts)

    @property
    def architecht(self) -> AsyncArchitecht:
        """Architecht (3 uç nokta)."""
        return self._resource("architecht", AsyncArchitecht)

    @property
    def cards(self) -> AsyncCards:
        """Kredi kartı işlemleri (4 uç nokta)."""
        return self._resource("cards", AsyncCards)

    @property
    def cash_management(self) -> AsyncCashManagement:
        """Nakit yönetimi (17 uç nokta)."""
        return self._resource("cash_management", AsyncCashManagement)

    @property
    def credibility(self) -> AsyncCredibility:
        """Kredibilite (5 uç nokta)."""
        return self._resource("credibility", AsyncCredibility)

    @property
    def donations(self) -> AsyncDonations:
        """Bağışlar (5 uç nokta)."""
        return self._resource("donations", AsyncDonations)

    @property
    def ecommerce(self) -> AsyncEcommerce:
        """E-ticaret (10 uç nokta)."""
        return self._resource("ecommerce", AsyncEcommerce)

    @property
    def financing(self) -> AsyncFinancing:
        """Finansman çözümleri (16 uç nokta)."""
        return self._resource("financing", AsyncFinancing)

    @property
    def fx(self) -> AsyncFx:
        """Döviz işlemleri (5 uç nokta)."""
        return self._resource("fx", AsyncFx)

    @property
    def hgs(self) -> AsyncHgs:
        """HGS servisleri (3 uç nokta)."""
        return self._resource("hgs", AsyncHgs)

    @property
    def information(self) -> AsyncInformation:
        """Bilgi servisleri (şube, ATM, parametre sorguları...) (12 uç nokta)."""
        return self._resource("information", AsyncInformation)

    @property
    def moneygram(self) -> AsyncMoneygram:
        """MoneyGram (6 uç nokta)."""
        return self._resource("moneygram", AsyncMoneygram)

    @property
    def other(self) -> AsyncOther:
        """Diğer (9 uç nokta)."""
        return self._resource("other", AsyncOther)

    @property
    def payment_solutions(self) -> AsyncPaymentSolutions:
        """Ödeme çözümleri (15 uç nokta)."""
        return self._resource("payment_solutions", AsyncPaymentSolutions)

    @property
    def payments(self) -> AsyncPayments:
        """Ödemeler (15 uç nokta)."""
        return self._resource("payments", AsyncPayments)

    @property
    def sgk(self) -> AsyncSgk:
        """SGK (1 uç nokta)."""
        return self._resource("sgk", AsyncSgk)

    @property
    def sms_otp(self) -> AsyncSmsOtp:
        """SMS / OTP (5 uç nokta)."""
        return self._resource("sms_otp", AsyncSmsOtp)

    @property
    def support(self) -> AsyncSupport:
        """Destek yönetimi (14 uç nokta)."""
        return self._resource("support", AsyncSupport)

    @property
    def tpp_accounts(self) -> AsyncTppAccounts:
        """Hesap yönetimi (TPP - müşteri adına) (5 uç nokta)."""
        return self._resource("tpp_accounts", AsyncTppAccounts)

    @property
    def transfers(self) -> AsyncTransfers:
        """Para transferleri (10 uç nokta)."""
        return self._resource("transfers", AsyncTransfers)

    @property
    def treasury(self) -> AsyncTreasury:
        """Hazine servisleri (kıymetli maden, kur) (5 uç nokta)."""
        return self._resource("treasury", AsyncTreasury)

    @property
    def vpos(self) -> AsyncVpos:
        """Sanal POS (15 uç nokta)."""
        return self._resource("vpos", AsyncVpos)

    @property
    def your_banking(self) -> AsyncYourBanking:
        """Senin Bankan (4 uç nokta)."""
        return self._resource("your_banking", AsyncYourBanking)
