#COMPUTING THE NEXT GREATER AND PREV GREATER INDICES FOR A INTERGER ARRAY  
#TIME :  O(N)
#SPACE : O(N)
def higher_ind(a):
  #NittinS Snippets  
  n=len(a)
    ans=[[-1,-1] for _ in range(n)]
    st=[]
    for i in range(n):
        while st and a[st[-1]]<=a[i]:
            st.pop()
        if st:
            ans[i][1]=st[-1]
        st.append(i)
    st=[]
    for i in range(n-1,-1,-1):
        while st and a[st[-1]]<=a[i]:
            st.pop()
        if st:
            ans[i][0]=st[-1]
        st.append(i)
    return ans


#COMPUTING THE NEXT LESSER AND PREV LESSER INDICES FOR A INTEGER ARRAY
#TIME :  O(N)
#SPACE : O(N)
def lower_ind(a):
#NittinS Snippets
    n=len(a)
    ans=[[-1,-1] for _ in range(n)]
    st=[]
    for i in range(n):
        while st and a[st[-1]]>=a[i]:
            st.pop()
        if st:
            ans[i][1]=st[-1]
        st.append(i)
    st=[]
    for i in range(n-1,-1,-1):
        while st and a[st[-1]]>=a[i]:
            st.pop()
        if st:
            ans[i][0]=st[-1]
        st.append(i)
    return ans

