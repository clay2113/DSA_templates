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


