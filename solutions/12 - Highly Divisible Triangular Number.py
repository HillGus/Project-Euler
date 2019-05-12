from time import process_time as pt
from primes import prime_factors as pf
from math import sqrt

def triangular(n):
    return int((n - 1) * (2 + (n - 4) / 2))

print(pt())

x = 2
while True:
    t = triangular(x)
    divisors = 0
    for x in range(1, int(sqrt(t))):
        if t % x == 0:
            divisors += 2
    if (divisors >= 500):
        print(divisors)
        print(t)
        break
    x += 1

print(pt())
