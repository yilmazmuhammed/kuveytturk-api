"""Uç nokta grupları ve istemcilere eklenen kaynak özellikleri.

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from ._resource import AsyncResource, Resource, ResourceHost
from .accounts import Accounts, AsyncAccounts
from .cards import AsyncCards, Cards
from .cash_management import AsyncCashManagement, CashManagement
from .fx import AsyncFx, Fx
from .hgs import AsyncHgs, Hgs
from .tpp_accounts import AsyncTppAccounts, TppAccounts
from .transfers import AsyncTransfers, Transfers
from .treasury import AsyncTreasury, Treasury
from .vpos import AsyncVpos, Vpos

__all__ = [
    "Accounts",
    "AsyncAccounts",
    "AsyncCards",
    "AsyncCashManagement",
    "AsyncFx",
    "AsyncHgs",
    "AsyncResource",
    "AsyncResourcesMixin",
    "AsyncTppAccounts",
    "AsyncTransfers",
    "AsyncTreasury",
    "AsyncVpos",
    "Cards",
    "CashManagement",
    "Fx",
    "Hgs",
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
    def fx(self) -> Fx:
        """Döviz işlemleri (5 uç nokta)."""
        return self._resource("fx", Fx)

    @property
    def hgs(self) -> Hgs:
        """HGS servisleri (1 uç nokta)."""
        return self._resource("hgs", Hgs)

    @property
    def tpp_accounts(self) -> TppAccounts:
        """Hesap yönetimi (TPP - müşteri adına) (4 uç nokta)."""
        return self._resource("tpp_accounts", TppAccounts)

    @property
    def transfers(self) -> Transfers:
        """Para transferleri (7 uç nokta)."""
        return self._resource("transfers", Transfers)

    @property
    def treasury(self) -> Treasury:
        """Hazine servisleri (kıymetli maden, kur) (5 uç nokta)."""
        return self._resource("treasury", Treasury)

    @property
    def vpos(self) -> Vpos:
        """Sanal POS (8 uç nokta)."""
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
    def fx(self) -> AsyncFx:
        """Döviz işlemleri (5 uç nokta)."""
        return self._resource("fx", AsyncFx)

    @property
    def hgs(self) -> AsyncHgs:
        """HGS servisleri (1 uç nokta)."""
        return self._resource("hgs", AsyncHgs)

    @property
    def tpp_accounts(self) -> AsyncTppAccounts:
        """Hesap yönetimi (TPP - müşteri adına) (4 uç nokta)."""
        return self._resource("tpp_accounts", AsyncTppAccounts)

    @property
    def transfers(self) -> AsyncTransfers:
        """Para transferleri (7 uç nokta)."""
        return self._resource("transfers", AsyncTransfers)

    @property
    def treasury(self) -> AsyncTreasury:
        """Hazine servisleri (kıymetli maden, kur) (5 uç nokta)."""
        return self._resource("treasury", AsyncTreasury)

    @property
    def vpos(self) -> AsyncVpos:
        """Sanal POS (8 uç nokta)."""
        return self._resource("vpos", AsyncVpos)
