from time import process_time as pt
from math import pow

print(pt())
print(pow(sum([x for x in range(1, 101)]), 2) - sum([pow(x, 2) for x in range(1, 101)]))
print(pt())
