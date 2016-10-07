def FindPrime(n):
    primes = [2, 3]
    for num in range(4, n):
        notprime = False
        for p in primes:
            if num % p == 0:
                notprime = True
        if notprime == False:
            primes.append(num)

    print (primes)

print (FindPrime(100))