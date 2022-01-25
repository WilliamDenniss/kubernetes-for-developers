from decimal import *

# Calculate pi using the Gregory-Leibniz infinity series
def leibniz_pi(iterations):

  precision = 20
  getcontext().prec = 20
  piDiv4 = Decimal(1)
  odd = Decimal(3)

  for i in range(0, iterations):
    piDiv4 = piDiv4 - 1/odd
    odd = odd + 2
    piDiv4 = piDiv4 + 1/odd
    odd = odd + 2

  return piDiv4 * 4
