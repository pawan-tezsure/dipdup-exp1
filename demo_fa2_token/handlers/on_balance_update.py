from dipdup.context import HandlerContext
from dipdup.models import BigMapDiff

import demo_fa2_token.models as models
from demo_fa2_token.types.fa2_type.big_map.assets_ledger_key import AssetsLedgerKey
from demo_fa2_token.types.fa2_type.big_map.assets_ledger_value import AssetsLedgerValue


async def on_balance_update(
    ctx: HandlerContext,
    assets_ledger: BigMapDiff[AssetsLedgerKey, AssetsLedgerValue],
) -> None:
    if(assets_ledger.key.nat != 10):
        return
    finalBalance = Decimal (assets_ledger.value.__root__) / (10 ** 18)
    newHolder, _ = await models.wLINKHolder.update_or_create(holderAddress = assets_ledger.key.address,defaults=dict(balance=finalBalance))