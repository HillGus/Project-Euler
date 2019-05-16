from commons import runtime
from math import sqrt

cache = {}
def divisors_sum(n):
    if n in cache:
        return cache[n]
    div_sum = 1
    for x in range(2, int(sqrt(n))):
        if n % x == 0:
            div_sum += x + n / x
    cache[n] = div_sum
    return div_sum

def amicable(n):
    div_sum = divisors_sum(n)
    if divisors_sum(div_sum) == n and div_sum != n:
        return n
    return 0

def resolve():
    total_sum = 0
    for n in range(1, 10000):
        total_sum += amicable(n)
    print(total_sum)

runtime(resolve)
