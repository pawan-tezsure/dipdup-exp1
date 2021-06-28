from dipdup.context import HandlerContext
from dipdup.models import BigMapDiff

import demo_plenty_token.models as models
from demo_plenty_token.types.plenty.big_map.balances_key import BalancesKey
from demo_plenty_token.types.plenty.big_map.balances_value import BalancesValue

from decimal import Decimal
async def on_balance_update(
    ctx: HandlerContext,
    balances: BigMapDiff[BalancesKey, BalancesValue],
) -> None:
    finalBalance = Decimal (balances.value.balance) / (10 ** 18)
    newHolder, _ = await models.Holder.update_or_create(holderAddress = balances.key.__root__,defaults=dict(balance=finalBalance))
