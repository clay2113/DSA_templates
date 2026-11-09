#DIGIT DP TEMPLATE FOR LC 600 PROBLEM WHERE I USE BINARY NUMBERS WITH STARTED CONDITION
class Solution:
    def findIntegers(self, n: int) -> int:
        s=bin(n)[2:]
        @cache
        def dp(pos,tight,prev,started):
            if pos==len(s):
                return 1
            limit=int(s[pos]) if tight else 1
            res=0
            for i in range(limit+1):
                if started:
                    if prev==-1:
                        res+=dp(pos+1,tight and limit==i,i,True)
                    else:
                        if prev!=i:
                            res+=dp(pos+1,tight and limit==i,i,False)
                else:
                    if i==0:            
                        res+=dp(pos+1,tight and limit==i,-1,False)
                    else:
                        res+=dp(pos+1,tight and limit==i,1,True) 
            return res
        return dp(0,True,-1,False) 
