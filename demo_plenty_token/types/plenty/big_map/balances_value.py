# generated by datamodel-codegen:
#   filename:  balances.value.json

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel


class BalancesValue(BaseModel):
    approvals: Dict[str, str]
    balance: str
