# %%
import decimal
from decimal import Decimal, getcontext

# 1.1 + 2.2
Decimal(1) / Decimal(7)

getcontext().prec = 4
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))
dir(Decimal)

1.1 + 2.2
getcontext().prec = 10
Decimal(1.1) + Decimal(2.2)

dir(decimal)
dir()
