from dipdup.context import HandlerContext
from dipdup.models import BigMapDiff

import demo_plenty_token.models as models
from demo_plenty_token.types.plenty.big_map.balances_key import BalancesKey
from demo_plenty_token.types.plenty.big_map.balances_value import BalancesValue


async def on_balance_update(
    ctx: HandlerContext,
    balances: BigMapDiff[BalancesKey, BalancesValue],
) -> None:
    print(BalancesKey)
    newHolder, _ = await models.Holder.get_or_create(holderAddress = BalancesKey)
    newHolder.balance = BalancesValue.balance
    await newHolder.save()