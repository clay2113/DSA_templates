from collections import Counter

contains -->  # behaves like: c in s
freq     -->  # Counter of alphabets in s[l:r]
count    -->  # frequency of c in s[l:r]
    class AlphaRange:
        # NittinS snippets
        def __init__(self,s):
            self.n=len(s)
            self.pref=[[0]*26 for _ in range(self.n+1)]
            for i,c in enumerate(s):
                self.pref[i+1]=self.pref[i].copy()
                self.pref[i+1][ord(c)-97]+=1
        def __contains__(self,c):
            x=ord(c)-97
            return any(self.pref[self.n][x:x+1])
        def freq(self,l,r):
            return Counter({
                chr(i+97):self.pref[r][i]-self.pref[l][i]
                for i in range(26)
                if self.pref[r][i]-self.pref[l][i]
            })
        def count(self,c,l,r):
            x=ord(c)-97
            return self.pref[r][x]-self.pref[l][x]
