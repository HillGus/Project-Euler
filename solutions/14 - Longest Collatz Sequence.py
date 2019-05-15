from time import process_time as pt
from commons import runtime

generated_chains = {}
def naive_fn(n):
    if generated_chains.get(n) != None:
        c = generated_chains.get(n)
        return c
    start = [n]
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    if n > 1:
        start.extend(naive_fn(n))
    generated_chains[n] = start
    return start

def naive_resolve():
    longest_chain = 0
    longest_owner = 0
    for x in range(999999, 1, -2):
        c = len(naive_fn(x)) + 1
        if c > longest_chain:
            longest_chain = c
            longest_owner = x
    print(longest_owner)

def new_fn(n):
    if generated_chains.get(n) != None:
        return generated_chains.get(n)
    length = 1
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    if n > 1:
        new_gen = new_fn(n)
        length += new_gen
        generated_chains[n] = new_gen
    return length + 1

def new_resolve():
    longest_chain = 0
    longest_owner = 0
    for x in range(999999, 1, -2):
        c = new_fn(x)
        if c > longest_chain:
            longest_chain = c
            longest_owner = x
    print(longest_owner)

runtime(new_resolve)
