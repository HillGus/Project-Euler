from math import sqrt

def rfactorial(n, until = 1):
    if n == until:
        return 1
    return n * factorial(n - 1)

def factorial(n):
    r = n
    for x in range(1, n // 2 + 1):
        r = r * x * (n - x)
    if n % 2 == 0:
        r = r // (n // 2)
    return r

def factors(n):
    factors_list = []
    for x in range(1, int(sqrt(n))):
        if n % x == 0:
            factors_list.append(x)
            factors_list.append(n // x)
    return factors
                   
def combination(n, c):
    return factorial(n) / (factorial(c) * factorial(n - c))
