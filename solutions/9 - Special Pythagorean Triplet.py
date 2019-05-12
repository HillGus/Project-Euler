from time import process_time as pt
from math import sqrt

print(pt())

for x in range(1, 1000):
    sbreak = False
    for y in range(1, 1000):
        z = sqrt(x * x + y * y)
        if z.is_integer():
            if x + y + z == 1000:
                print(x, y, z)
                print (x * y * z)
                sbreak = True
                break
    if sbreak:
        break
print(pt())
