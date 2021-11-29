from decimal import Decimal, ROUND_HALF_UP
import decimal
def round_by_2_decimal_places(n):
    number = decimal.getcontext()  #https://docs.python.org/es/3/library/decimal.html
    number.rounding =decimal.ROUND_HALF_UP
    return round(n,2)

