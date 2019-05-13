from commons import runtime
from mathh import factorial

def resolve():
    print(sum([int(c) for c in str(factorial(100))]))

runtime(resolve)
