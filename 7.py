# Note: I don't know how to write efficient code, but it works
# I think that this is O(n^3)

primes = [2]
j = 3

while len(primes) < 10001:
    i = j
    for prime in primes:
        while i%prime==0:
            i = i / prime

    if i != 1:
        primes.append(j)
    j += 2 # skips even numbers

print(primes[-1])        


