from time import process_time as pt

print(pt())

def factorial(n, until = 1):
    if n == until:
        return 1
    return n * factorial(n - 1)

print(factorial(40) / (factorial(20) * factorial(20)))

print(pt())
