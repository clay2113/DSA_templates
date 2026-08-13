"""64-BIT POLYNOMIAL ROLLING HASH"""    # SUBARRAY EQUALITY

# Build: O(N)
# Subarray Hash: O(1)
# Compare Subarrays: O(1)
# Space: O(N)

    class RollingHash64:
        #NittinS Snippets
        MASK=(1<<64)-1
        def splitmix64(self,x):
            x&=self.MASK
            x=(x+0x9e3779b97f4a7c15)&self.MASK
            x=(x^(x>>30))*0xbf58476d1ce4e5b9&self.MASK
            x=(x^(x>>27))*0x94d049bb133111eb&self.MASK
            return (x^(x>>31))&self.MASK
        def __init__(self,a):
            self.n=len(a)
            self.MASK=(1<<64)-1
            self.BASE=self.splitmix64(123456789)|1
            self.pow=[1]*(self.n+1)
            self.pref=[0]*(self.n+1)
            for i in range(self.n):
                self.pow[i+1]=(self.pow[i]*self.BASE)&self.MASK
                self.pref[i+1]=((self.pref[i]*self.BASE)+self.splitmix64(a[i]))&self.MASK
        def hash(self,l,r):
            return (self.pref[r+1]-(self.pref[l]*self.pow[r-l+1]))&self.MASK
        def equal(self,l1,r1,l2,r2):
            if r1-l1!=r2-l2:
                return False
            return self.hash(l1,r1)==self.hash(l2,r2)


# REPEATED ROLLING HASH
# NittinS Snippets
# APPEND : O(1)
# HASH : O(1)
# SPACE : O(1)

    class RollingHash:
        #NittinS snippets
        def __init__(self,base=911382323,mod=10**18+9):
            self.base=base
            self.mod=mod
            self.hash=0
    
        def add(self,c):
            if isinstance(c,str):
                c=ord(c)
            self.hash=(self.hash*self.base+c)%self.mod
    
        def get(self):
            return self.hash


# REPEATED DOUBLE ROLLING HASH
# NittinS Snippets
# APPEND : O(1)
# HASH : O(1)
# SPACE : O(1)

    class RollingHash:
        #NittinS snippets
        def __init__(self):
            self.h1=0
            self.h2=0
            self.b1=911382323
            self.b2=972663749
            self.m1=(1<<64)
            self.m2=(1<<64)

        def add(self,c):
            if isinstance(c,str):
                c=ord(c)
            self.h1=(self.h1*self.b1+c)%self.m1
            self.h2=(self.h2*self.b2+c)%self.m2

        def get(self):
            return self.h1,self.h2
