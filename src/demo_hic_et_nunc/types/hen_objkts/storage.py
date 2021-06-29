# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel


class Key(BaseModel):
    address: str
    nat: str


class LedgerItem(BaseModel):
    key: Key
    value: str


class Key1(BaseModel):
    operator: str
    owner: str
    token_id: str


class Operator(BaseModel):
    key: Key1
    value: Dict[str, Any]


class TokenMetadata(BaseModel):
    token_id: str
    token_info: Dict[str, str]


class HenObjktsStorage(BaseModel):
    administrator: str
    all_tokens: str
    ledger: List[LedgerItem]
    metadata: Dict[str, str]
    operators: List[Operator]
    paused: bool
    token_metadata: Dict[str, TokenMetadata]
