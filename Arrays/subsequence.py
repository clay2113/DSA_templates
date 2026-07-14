#LONGEST PALINDROMIC SUBSEQUENCES   ---> N^2 SOLUTION
    def lps(s):
        #NittinS Snippets
        dp=[[0 if i<=j else float("-inf") for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=1
        for i in range(len(s)-1):
            dp[i][i+1]=2 if s[i]==s[i+1] else 1
        for i in range(3,len(s)+1):
            for j in range(len(s)-i+1):
                if s[j]==s[j+i-1]:
                    dp[j][j+i-1]=2+dp[j+1][j+i-2]
                dp[j][j+i-1]=max(dp[j][j+i-1],dp[j][j+i-2],dp[j+1][j+i-1])
        return dp[0][len(s)-1]


#LONGEST COMMON SUBSEQUNCE    N*M TIME
def lcs(t1,t2):
    #NittinS snippets
    n,m=len(t1),len(t2)
    prev=[0]*(m+1)
    for i in range(1,n+1):
        cur=[0]*(m+1)
        for j in range(1,m+1):
            if t1[i-1]==t2[j-1]:
                cur[j]=1+prev[j-1]
            else:
                cur[j]=max(prev[j],cur[j-1])
        prev=cur
    return prev[m]


#LONGEST INCREASING SUBSEQUENCE    N^2 TIME
def lis_n2(nums):
    #NittinS snippets
    n=len(nums)

    dp=[1]*n

    for i in range(n):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp) if nums else 0


#LONGEST INCREASING SUBSEQUENCE NLOGN
#TC: O(nlogn)
#SC: O(n)
def lis_nlogn(nums):
    #NittinS snippets
    tails=[]
    for x in nums:
        idx=bisect_left(tails,x)
        if idx==len(tails):
            tails.append(x)
        else:
            tails[idx]=x
    return len(tails)
