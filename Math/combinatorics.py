#CHOOSING NUMBER OF PAIRS FROM A LIST OF OBJECTS FORMULA:
cnt=(n*(n-1))//2


#Combination with mod
class Comb:
    #NittinS snippets
    def __init__(self,N,MOD=10**9+7):
        self.MOD=MOD
        self.fact=[1]*(N+1)
        self.invfact=[1]*(N+1)
        for i in range(1,N+1):
            self.fact[i]=self.fact[i-1]*i%MOD
        self.invfact[N]=pow(self.fact[N],MOD-2,MOD)
        for i in range(N,0,-1):
            self.invfact[i-1]=self.invfact[i]*i%MOD
    def C(self,n,r):
        if r<0 or r>n:
            return 0
        return self.fact[n]*self.invfact[r]%self.MOD*self.invfact[n-r]%self.MOD
