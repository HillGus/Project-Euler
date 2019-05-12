import time

print(time.process_time())
discovered = {}

def fib(d):
    if d == 1 or d == 0:
        return 1
    else:
        if discovered.get(d) != None:
            return discovered.get(d)
        result = fib(d - 1) + fib(d - 2)
        discovered[d] = result
        return result
    
soma = 0
for x in range(1, 4000000):
    result = fib(x)
    if (result > 4000000):
        break
    soma += result if result % 2 == 0 else 0
print(soma)
print(time.process_time())
