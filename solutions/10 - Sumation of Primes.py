from time import process_time as pt
from primes import primes_until

print(pt())

print(sum(primes_until(2000000)))

print(pt())
