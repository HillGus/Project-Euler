from time import process_time as pt

print(pt())
palindrome = []
for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        n = str(x * y)
        if n == n[::-1]:
            palindrome.append(int(n))
print(max(palindrome))
print(pt())
