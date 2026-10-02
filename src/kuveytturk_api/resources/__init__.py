"""Uç nokta grupları ve istemcilere eklenen kaynak özellikleri.

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from ._resource import AsyncResource, Resource, ResourceHost
from .accounts import Accounts, AsyncAccounts
from .cards import AsyncCards, Cards
from .cash_management import AsyncCashManagement, CashManagement
from .donations import AsyncDonations, Donations
from .ecommerce import AsyncEcommerce, Ecommerce
from .financing import AsyncFinancing, Financing
from .fx import AsyncFx, Fx
from .hgs import AsyncHgs, Hgs
from .information import AsyncInformation, Information
from .other import AsyncOther, Other
from .payment_solutions import AsyncPaymentSolutions, PaymentSolutions
from .payments import AsyncPayments, Payments
from .tpp_accounts import AsyncTppAccounts, TppAccounts
from .transfers import AsyncTransfers, Transfers
from .treasury import AsyncTreasury, Treasury
from .vpos import AsyncVpos, Vpos

__all__ = [
    "Accounts",
    "AsyncAccounts",
    "AsyncCards",
    "AsyncCashManagement",
    "AsyncDonations",
    "AsyncEcommerce",
    "AsyncFinancing",
    "AsyncFx",
    "AsyncHgs",
    "AsyncInformation",
    "AsyncOther",
    "AsyncPaymentSolutions",
    "AsyncPayments",
    "AsyncResource",
    "AsyncResourcesMixin",
    "AsyncTppAccounts",
    "AsyncTransfers",
    "AsyncTreasury",
    "AsyncVpos",
    "Cards",
    "CashManagement",
    "Donations",
    "Ecommerce",
    "Financing",
    "Fx",
    "Hgs",
    "Information",
    "Other",
    "PaymentSolutions",
    "Payments",
    "Resource",
    "ResourcesMixin",
    "TppAccounts",
    "Transfers",
    "Treasury",
    "Vpos",
]


class ResourcesMixin(ResourceHost):
    """Senkron istemcinin kaynak özellikleri (``kt.accounts`` gibi)."""

    @property
    def accounts(self) -> Accounts:
        """Hesap yönetimi (kurumun kendi hesapları) (6 uç nokta)."""
        return self._resource("accounts", Accounts)

    @property
    def cards(self) -> Cards:
        """Kredi kartı işlemleri (3 uç nokta)."""
        return self._resource("cards", Cards)

    @property
    def cash_management(self) -> CashManagement:
        """Nakit yönetimi (17 uç nokta)."""
        return self._resource("cash_management", CashManagement)

    @property
    def donations(self) -> Donations:
        """Bağışlar (4 uç nokta)."""
        return self._resource("donations", Donations)

    @property
    def ecommerce(self) -> Ecommerce:
        """E-ticaret (10 uç nokta)."""
        return self._resource("ecommerce", Ecommerce)

    @property
    def financing(self) -> Financing:
        """Finansman çözümleri (4 uç nokta)."""
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
        """Bilgi servisleri (şube, ATM, parametre sorguları...) (1 uç nokta)."""
        return self._resource("information", Information)

    @property
    def other(self) -> Other:
        """Diğer (2 uç nokta)."""
        return self._resource("other", Other)

    @property
    def payment_solutions(self) -> PaymentSolutions:
        """Ödeme çözümleri (14 uç nokta)."""
        return self._resource("payment_solutions", PaymentSolutions)

    @property
    def payments(self) -> Payments:
        """Ödemeler (14 uç nokta)."""
        return self._resource("payments", Payments)

    @property
    def tpp_accounts(self) -> TppAccounts:
        """Hesap yönetimi (TPP - müşteri adına) (5 uç nokta)."""
        return self._resource("tpp_accounts", TppAccounts)

    @property
    def transfers(self) -> Transfers:
        """Para transferleri (8 uç nokta)."""
        return self._resource("transfers", Transfers)

    @property
    def treasury(self) -> Treasury:
        """Hazine servisleri (kıymetli maden, kur) (5 uç nokta)."""
        return self._resource("treasury", Treasury)

    @property
    def vpos(self) -> Vpos:
        """Sanal POS (15 uç nokta)."""
        return self._resource("vpos", Vpos)


class AsyncResourcesMixin(ResourceHost):
    """Asenkron istemcinin kaynak özellikleri (``kt.accounts`` gibi)."""

    @property
    def accounts(self) -> AsyncAccounts:
        """Hesap yönetimi (kurumun kendi hesapları) (6 uç nokta)."""
        return self._resource("accounts", AsyncAccounts)

    @property
    def cards(self) -> AsyncCards:
        """Kredi kartı işlemleri (3 uç nokta)."""
        return self._resource("cards", AsyncCards)

    @property
    def cash_management(self) -> AsyncCashManagement:
        """Nakit yönetimi (17 uç nokta)."""
        return self._resource("cash_management", AsyncCashManagement)

    @property
    def donations(self) -> AsyncDonations:
        """Bağışlar (4 uç nokta)."""
        return self._resource("donations", AsyncDonations)

    @property
    def ecommerce(self) -> AsyncEcommerce:
        """E-ticaret (10 uç nokta)."""
        return self._resource("ecommerce", AsyncEcommerce)

    @property
    def financing(self) -> AsyncFinancing:
        """Finansman çözümleri (4 uç nokta)."""
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
        """Bilgi servisleri (şube, ATM, parametre sorguları...) (1 uç nokta)."""
        return self._resource("information", AsyncInformation)

    @property
    def other(self) -> AsyncOther:
        """Diğer (2 uç nokta)."""
        return self._resource("other", AsyncOther)

    @property
    def payment_solutions(self) -> AsyncPaymentSolutions:
        """Ödeme çözümleri (14 uç nokta)."""
        return self._resource("payment_solutions", AsyncPaymentSolutions)

    @property
    def payments(self) -> AsyncPayments:
        """Ödemeler (14 uç nokta)."""
        return self._resource("payments", AsyncPayments)

    @property
    def tpp_accounts(self) -> AsyncTppAccounts:
        """Hesap yönetimi (TPP - müşteri adına) (5 uç nokta)."""
        return self._resource("tpp_accounts", AsyncTppAccounts)

    @property
    def transfers(self) -> AsyncTransfers:
        """Para transferleri (8 uç nokta)."""
        return self._resource("transfers", AsyncTransfers)

    @property
    def treasury(self) -> AsyncTreasury:
        """Hazine servisleri (kıymetli maden, kur) (5 uç nokta)."""
        return self._resource("treasury", AsyncTreasury)

    @property
    def vpos(self) -> AsyncVpos:
        """Sanal POS (15 uç nokta)."""
        return self._resource("vpos", AsyncVpos)
