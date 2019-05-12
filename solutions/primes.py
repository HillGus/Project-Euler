from math import sqrt 
prime_list = [2, 3]
def is_prime(x):
    if not ((x - 1) % 6 == 0 or (x + 1) % 6 == 0):
        return False
    for p in prime_list:
        if p > int(sqrt(x)) or p == x:
            break
        if x % p == 0:
            return False
    prime_list.append(x)
    return True

def primes():
    for x in range(0, len(prime_list)):
	    yield prime_list[x], x
    x = prime_list[-1] + 2
    while True:
        if is_prime(x):
            yield x , len(prime_list)
        x += 2

def primes_until(x):
    limitn = x+1
    not_prime_num = set()
    prime_nums = []
    for i in range(2, limitn):
        if i in not_prime_num:
            continue
        for f in range(i*2, limitn, i):
            not_prime_num.add(f)
        prime_nums.append(i)
    return prime_nums

def prime_factors(x):
    factors = []
    y = 3
    while x > 1:
        for p, i in primes():
            while x % p == 0:
                x /= p
                if p not in factors:
                    factors.append(p)
            if x == 1:
                break
    return factors
