
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
            #NittinS snippets --> https://github.com/clay2113/DSA_templates
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



#IF A,B, ... IS ALREADY MODDED WITH 10**9+7 THEN EVALUATE (A-B-C...)%MOD
#this works because the addition and subtraction is closed by mod opertaion
val=(A-B-C)%MOD





#IF A IS ALREADY MODDED WITH MOD THEN EVALUATE (A/B)%MOD

#in this case you have to create something called as the inverse mod thingy that behaves like a normal 
#multiplicative mod
#If the modulus is prime (such as 10**9+7), you can compute the modular inverse in O(log MOD) time using binary exponentiation and Fermat's Little Theorem.

MOD=10**9+7
inv=pow(a,MOD-2,MOD)
print((5*inv)%MOD)
#Time: O(log MOD)
#Space: O(1)



#TO SOLVE --> (x*c) mod m =0 solve for x where c is constant  LC 2183
for all x which are divisible by m/gcd(x,m) satisfies the equation 
#KEEP IN MIND THAT ALL POSSIBLE M/GCD(X,M) CAN BE LIKE MAX 100 DISTINCT NUMBERS SO U CAN APPLY IN 10**5 NUMBERS ALSO 
#The number below 100,000 with the most factors is 83,160, which has a total of 128 factors.



#IF WE NEED TO FIND THE MODULAR INVERSE OF A (X/Y) MOD M  FOR Y  THEN FOR ANY M WHERE GCD(Y,M) ==1
from math import gcd

def mod_div(x,y,m):
    if gcd(y,m)!=1:
        return None
    return (x%m)*pow(y,-1,m)%m

#BASIC MOD ADD AND SUBTRACT 
-> (a + b)%k = (a%k + b%k)%k 
-> (a - b)%k = (a%k - b%k + k)%k

