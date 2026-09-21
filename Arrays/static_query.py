"""STATIC MAX SPARSE TABLE"""    # RANGE MAX QUERY

# Build: O(N log N)
# Range max query: O(1)
# Memory: O(N log N)

class StaticMax:
    #NittinS snippets
    def __init__(self,a):
        self.n=len(a)
        self.LOG=self.n.bit_length()

        self.st=[a[:]]

        for j in range(1,self.LOG):
            prev=self.st[-1]
            length=1<<j
            half=length>>1

            self.st.append([
                max(prev[i],prev[i+half])
                for i in range(self.n-length+1)
            ])

        self.log=[0]*(self.n+1)
        for i in range(2,self.n+1):
            self.log[i]=self.log[i>>1]+1

    def max_val(self,l,r):
        k=self.log[r-l+1]
        return max(self.st[k][l],self.st[k][r-(1<<k)+1])



"""STATIC MIN SPARSE TABLE"""    # RANGE MIN QUERY

# Build: O(N log N)
# Range min query: O(1)
# Memory: O(N log N)

class StaticMin:
    #NittinS snippets
    def __init__(self,a):
        self.n=len(a)
        self.LOG=self.n.bit_length()

        self.st=[a[:]]

        for j in range(1,self.LOG):
            prev=self.st[-1]
            length=1<<j
            half=length>>1

            self.st.append([
                min(prev[i],prev[i+half])
                for i in range(self.n-length+1)
            ])

        self.log=[0]*(self.n+1)
        for i in range(2,self.n+1):
            self.log[i]=self.log[i>>1]+1

    def min_val(self,l,r):
        # inclusive [l,r]
        k=self.log[r-l+1]
        return min(self.st[k][l],self.st[k][r-(1<<k)+1])



"""STATIC XOR SPARSE TABLE"""    # RANGE XOR QUERY

# Build: O(N log N)
# Range xor query: O(log N)
# Memory: O(N log N)

class StaticXor:
    #NittinS snippets
    def __init__(self,a):
        self.n=len(a)
        self.LOG=self.n.bit_length()

        self.st=[a[:]]

        for j in range(1,self.LOG):
            prev=self.st[-1]
            length=1<<j
            half=length>>1

            self.st.append([
                prev[i]^prev[i+half]
                for i in range(self.n-length+1)
            ])

        self.log=[0]*(self.n+1)
        for i in range(2,self.n+1):
            self.log[i]=self.log[i>>1]+1

    def xor_val(self,l,r):
        # inclusive [l,r]
        ans=0

        for j in range(self.LOG-1,-1,-1):
            length=1<<j

            if length<=r-l+1:
                ans^=self.st[j][l]
                l+=length

        return ans
