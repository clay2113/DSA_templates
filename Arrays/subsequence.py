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
