from time import process_time as pt
from commons import runtime
from math import log

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

generated_lengths = {}
def new_fn(n):
    if n in generated_lengths:
        return generated_lengths[n]
    length = 1
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    if n > 1:
        new_gen = new_fn(n)
        length += new_gen
        generated_lengths[n] = new_gen
    return length

def new_resolve():
    longest_chain = 0
    longest_owner = 0
    for x in range(500001, 999999, 2):
        c = new_fn(x)
        if c > longest_chain:
            longest_chain = c
            longest_owner = x
    print(longest_owner)

thread_generated_lengths = {1:1}
def thread_fn(n):
    if n not in thread_generated_lengths:
        thread_generated_lengths[n] = thread_fn(n // 2) + 1  if n % 2 == 0 else thread_fn((3 * n + 1) // 2) + 2
    return thread_generated_lengths[n]

def thread_resolve():
    longest_chain = 0
    longest_owner = 0
    for x in range(1, 1000000):
        c = thread_fn(x)
        if c > longest_chain:
            longest_chain = c
            longest_owner = x
    print(longest_owner)

runtime(new_resolve)
