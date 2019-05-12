from time import process_time as pt
from primes import primes

print(pt())
for p, i in primes():
    if i == 100001:
        print(p)
        break
print(pt())


