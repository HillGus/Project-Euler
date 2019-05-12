from time import process_time as pt

print(pt())

generated_chains = {}
def chain(n):
    if generated_chains.get(n) != None:
        return generated_chains.get(n)
    start = [n]
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    if n > 1:
        start.extend(chain(int(n)))
    generated_chains[n] = start
    return start

longest_chain = 0
longest_owner = 0
for x in range(999999, 1, -2):
    c = len(chain(x) + [1])
    if c > longest_chain:
        longest_chain = c
        longest_owner = x
print(longest_owner)
print(pt())
