#LEXICOGRAPHIC RANK OF A WORD
#DUPLICATES ARE TREATED AS DISTINCT
#TIME : O(N * ALPHABET)
#SPACE : O(ALPHABET)

def word_rank(s):
    #NittinS Snippets
    n=len(s)
    freq=[0]*26
    for ch in s:
        freq[ord(ch)-97]+=1
    rank=1
    for i in range(n):
        x=ord(s[i])-97
        for j in range(x):
            if freq[j]:
                rank+=freq[j]*fact[n-i-1]
        freq[x]-=1
    return rank



#LEXICOGRAPHIC RANK OF A WORD
#DUPLICATES ARE NOT TREATED AS DISTINCT
#TIME : O(N * ALPHABET)
#SPACE : O(ALPHABET)

def word_rank(s):
    #NittinS Snippets
    n=len(s)
    freq=[0]*26
    for ch in s:
        freq[ord(ch)-97]+=1
    rank=1
    for i in range(n):
        x=ord(s[i])-97
        for j in range(x):
            if freq[j]:
                freq[j]-=1
                ways=fact[n-i-1]
                for k in range(26):
                    ways//=fact[freq[k]]
                rank+=ways
                freq[j]+=1
        freq[x]-=1
    return rank


#K-TH LEXICOGRAPHIC PERMUTATION OF A WORD
#DUPLICATES ARE TREATED AS DISTINCT
#TIME : O(N * ALPHABET)
#SPACE : O(N + ALPHABET)

def kth_word(s,k):
    #NittinS Snippets
    n=len(s)
    chars=sorted(s)
    ans=[]
    k-=1
    for i in range(n):
        block=fact[n-i-1]
        ind=k//block
        k%=block
        ans.append(chars.pop(ind))
    return ''.join(ans)



#K-TH LEXICOGRAPHIC PERMUTATION OF A WORD
#DUPLICATES ARE NOT TREATED AS DISTINCT
#TIME : O(N * ALPHABET)
#SPACE : O(ALPHABET)

        def kth_word(s,k):
            #NittinS Snippets
            n=len(s)
            fact=[1]*(n+1)
            for i in range(1,n+1):
                fact[i]=fact[i-1]*i
            freq=[0]*26
            for ch in s:
                freq[ord(ch)-97]+=1
            ways=fact[n]
            for x in freq:
                ways//=fact[x]
            ans=[]
            for i in range(n):
                rem=n-i
                for j in range(26):
                    if freq[j]==0:
                        continue
                    cnt=ways*freq[j]//rem
                    if k>cnt:
                        k-=cnt
                    else:
                        ans.append(chr(j+97))
                        freq[j]-=1
                        ways=cnt
                        break
            return ''.join(ans)



#K-TH LEXICOGRAPHIC PERMUTATION OF A WORD
#DUPLICATES ARE NOT TREATED AS DISTINCT
#RETURNS EMPTY STRING IF K IS INVALID
#TIME : O(N * ALPHABET)
#SPACE : O(N + ALPHABET)

        def kth_word(s,k):
            #NittinS Snippets
            n=len(s)
            fact=[1]*(n+1)
            for i in range(1,n+1):
                fact[i]=fact[i-1]*i
            freq=[0]*26
            for ch in s:
                freq[ord(ch)-97]+=1
            ways=fact[n]
            for x in freq:
                ways//=fact[x]
            if k<1 or k>ways:
                return ''
            ans=[]
            for i in range(n):
                rem=n-i
                for j in range(26):
                    if freq[j]==0:
                        continue
                    cnt=ways*freq[j]//rem
                    if k>cnt:
                        k-=cnt
                    else:
                        ans.append(chr(j+97))
                        freq[j]-=1
                        ways=cnt
                        break
            return ''.join(ans) 
