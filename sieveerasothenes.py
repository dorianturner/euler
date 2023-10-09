def PrimesLessThan(n):
    primes = [True for i in range(n+1)]

    p = 2
    while(p*p<=n):
        if primes[p]==True:
            for i in range (p*2,n+1,p):
                primes[i] = False
        p+=1
    
    nprimes = []
    for p in range(2,n+1):
        if primes[p]:
            nprimes.append(p)

    return nprimes



print(PrimesLessThan(50))