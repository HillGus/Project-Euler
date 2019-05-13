from time import process_time as pt
from commons import runtime

generated_chains = {}
def naive(n):
    if generated_chains.get(n) != None:
        c = generated_chains.get(n)
        return c
        #if c[-1] != 1:
        #    return c.extend(chain(c[-1]))
    start = [n]
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    if n > 1:
        start.extend(naive(int(n)))
    generated_chains[n] = start
    return start

def new(n):
    if generated_chains.get(n) != None:
        c = generated_chains.get(n)
        return c
        if c[-1] != 1:
            return c.extend(new(c[-1]))
    start = [n]
    old_n = n
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    if n > 1:
        generated_chains[old_n] = list(start)
        start.extend(new(int(n)))
    return start

def resolve():
    longest_chain = 0
    longest_owner = 0
    for x in range(999999, 1, -2):
        c = len(new(x) + [1])
        if c > longest_chain:
            longest_chain = c
            longest_owner = x
    print(longest_owner)
    print(sum([len(generated_chains[x]) for x in generated_chains]))

runtime(resolve)
