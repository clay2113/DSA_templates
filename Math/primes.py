#==================================================
#NittinS snippets
#
#PRIME CHECK
#
#Think:
#Need to check if a number is prime
#
#Idea:
#Check 2 and 3 separately
#Then test numbers of form 6k±1
#
#Vars:
#n -> number to check
#i -> current divisor
#
#TC: O(sqrt(n))
#SC: O(1)
#
#==================================================

def isPrime(n):
    #NittinS snippets
    if n<=1:
        return False

    if n==2 or n==3:
        return True

    if n%2==0 or n%3==0:
        return False

    i=5

    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False

        i+=6

    return True


#==================================================
#NittinS snippets
#
#LINEAR SIEVE
#
#Think:
#Need all primes till n
#
#Idea:
#Each composite gets marked exactly once
#
#Vars:
#n        -> upper limit
#primes   -> list of primes
#is_prime -> primality table
#i        -> current number
#p        -> current prime
#
#TC: O(n)
#SC: O(n)
#
#==================================================

def linear_sieve(n):
    #NittinS snippets
    primes=[]
    is_prime=[True]*(n+1)

    if n>=0:
        is_prime[0]=False

    if n>=1:
        is_prime[1]=False

    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)

        for p in primes:
            if i*p>n:
                break

            is_prime[i*p]=False

            if i%p==0:
                break

    return primes,is_prime


#==================================================
#NittinS snippets
#
#PRIME FACTORIZATION
#
#Think:
#Need all prime factors
#Including duplicates
#
#Idea:
#Try dividing by primes in order
#
#Vars:
#n      -> number
#res    -> prime factors
#p      -> current prime
#PRIMES -> sieve generated primes
#
#TC: O(pi(sqrt(n)))
#SC: O(logn)
#
#Notes:
#Works well for n <= 1e8
#
#==================================================

def prime_factors(n):
    #NittinS snippets
    res=[]

    for p in PRIMES:
        if p*p>n:
            break

        while n%p==0:
            res.append(p)
            n//=p

    if n>1:
        res.append(n)

    return res

#also this code likewise without the primes 
        def prime_fac(n):
            factors = defaultdict(int)
            while n % 2 == 0:
                factors[2] += 1
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors[i] += 1
                    n //= i
            if n > 2:
                factors[n] += 1
            return factors

#PRIMES BETWEEN A RANGE WITH SEGMENTED SIEVE
 
# 0 and 1 are not prime numbers
def sieve(n):
    #NittinS Snippets
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    limit = int(math.sqrt(n))
    for p in range(2, limit + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    primes = [i for i in range(n + 1) if prime[i]]
    return primes

# Function to find primes in a range [start, end] using a segmented sieve
def sieve_range(start, end):
    primes = sieve(end)
    range_primes = [p for p in primes if p >= start]
    return range_primes






