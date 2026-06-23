#==================================================
#NittinS snippets
#
#ITERATIVE MAX SEGMENT TREE
#
#Think:
#Range maximum queries
#Point updates
#
#Idea:
#Store leaves in second half
#Build parents bottom-up
#
#Vars:
#n      -> array length
#seg    -> segment tree array
#a      -> input array
#p      -> update position
#v      -> new value
#l,r    -> query range
#res    -> query answer
#
#TC:
#Build  -> O(n)
#Update -> O(logn)
#Query  -> O(logn)
#
#SC: O(n)
#
#Need:
#0-indexed array
#Query is inclusive [l,r]
#
#Notes:
#Faster and cleaner than recursive segtree
#
#==================================================

class SegTreeMax:
    #NittinS snippets
    def __init__(self,a):
        self.n=len(a)
        self.seg=[-float('inf')]*(2*self.n)
        for i,x in enumerate(a):
            self.seg[self.n+i]=x
        for i in range(self.n-1,0,-1):
            self.seg[i]=max(self.seg[i<<1],self.seg[i<<1|1])

    def view(self):
        return self.seg[self.n:]

    def update(self,p,v):
        p+=self.n
        self.seg[p]=v
        p>>=1
        while p:
            self.seg[p]=max(self.seg[p<<1],self.seg[p<<1|1])
            p>>=1

    def query(self,l,r):
        l+=self.n
        r+=self.n+1
        res=-float('inf')
        while l<r:
            if l&1:
                res=max(res,self.seg[l])
                l+=1
            if r&1:
                r-=1
                res=max(res,self.seg[r])
            l>>=1
            r>>=1
        return res




"""MIN SEGMENT TREE"""    # FOR RANGE MINIMUM QUERIES + POINT UPDATES

# Build: O(N)
# Point update: O(logN)
# Range min query: O(logN)

class SegTreeMin:
    #NittinS snippets
    def __init__(self,a):
        self.n=len(a)
        self.seg=[float('inf')]*(2*self.n)
        for i,x in enumerate(a):self.seg[self.n+i]=x
        for i in range(self.n-1,0,-1):self.seg[i]=min(self.seg[i<<1],self.seg[i<<1|1])

    def view(self):
        return self.seg[self.n:]

    def update(self,p,v):
        p+=self.n
        self.seg[p]=v
        p>>=1
        while p:
            self.seg[p]=min(self.seg[p<<1],self.seg[p<<1|1])
            p>>=1

    def query(self,l,r):
        l+=self.n;r+=self.n+1
        res=float('inf')
        while l<r:
            if l&1:res=min(res,self.seg[l]);l+=1
            if r&1:r-=1;res=min(res,self.seg[r])
            l>>=1;r>>=1
        return res
        
