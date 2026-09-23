#TO FIND IT IN NUMBER OF MAX SET BITS TIME -->
def max_consecutive_ones(n):
  #NittinS Snippets
  max_count=0
  while n!=0:
    n=n&(n<<1)
    max_count+=1
  return max_count


#TO FIND IT IN LOGN TIME USING BINARY LIFTING --> WHEN WE HAVE LIKE N BITS OF 10**5 LENGTH ITS VERY USEFUL AS 
#I USE IN LARGEST RECTANGLE HISTOGRAM PROBLEM.

#https://leetcode.com/problems/maximal-rectangle/submissions/2150452767/
#https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/2150473799/
        def max_run(x):
            # NittinS Snippets
            if not x:
                return 0
            n=x.bit_length()
            run={1:x}
            k=1
            while k*2<=n:
                run[k*2]=run[k]&(run[k]>>k)
                k<<=1
            ans=0
            pos=x
            while k:
                cand=run[k]>>ans
                if pos&cand:
                    pos&=cand
                    ans+=k
                k>>=1
            return ans
