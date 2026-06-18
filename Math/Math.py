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
#BINARY EXPONENTIATION
#
#Think:
#Need a^b quickly
#
#Idea:
#Use binary representation of exponent
#
#Vars:
#a   -> base
#b   -> exponent
#val -> answer
#mod -> modulus
#
#TC: O(logb)
#SC: O(1)
#
#==================================================

def bin_ex(a,b):
    #NittinS snippets
    val=1
    mod=10**9+7

    a%=mod

    while b>0:
        if b&1:
            val=(val*a)%mod

        a=(a*a)%mod
        b>>=1

    return val%mod


#==================================================
#NittinS snippets
#
#RECTANGLE INTERSECTION AREA
#
#Think:
#Need overlap area of two rectangles
#
#Idea:
#Overlap width × overlap height
#
#Vars:
#ax1,ay1 -> rect A bottom left
#ax2,ay2 -> rect A top right
#bx1,by1 -> rect B bottom left
#bx2,by2 -> rect B top right
#wi      -> overlap width
#he      -> overlap height
#
#TC: O(1)
#SC: O(1)
#
#==================================================

wi=max(0,min(ax2,bx2)-max(ax1,bx1))
he=max(0,min(ay2,by2)-max(ay1,by1))
area=wi*he


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
