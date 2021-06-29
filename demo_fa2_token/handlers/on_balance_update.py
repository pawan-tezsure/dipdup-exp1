from dipdup.context import HandlerContext
from dipdup.models import BigMapDiff

import demo_fa2_token.models as models
from demo_fa2_token.types.fa2_type.big_map.assets_ledger_key import AssetsLedgerKey
from demo_fa2_token.types.fa2_type.big_map.assets_ledger_value import AssetsLedgerValue


async def on_balance_update(
    ctx: HandlerContext,
    assets_ledger: BigMapDiff[AssetsLedgerKey, AssetsLedgerValue],
) -> None:
    ...