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


"""LAZY MIN SEGMENT TREE"""    # RANGE ADD + RANGE MIN QUERY

# Build: O(N)
# Range add: O(logN)
# Range min query: O(logN)

    class LazyMin:
    #NittinS snippets
        def __init__(self,a):
            self.n=len(a)
            self.seg=[0]*(4*self.n)
            self.lazy=[0]*(4*self.n)
            def build(i,l,r):
                if l==r:
                    self.seg[i]=a[l]
                    return
                m=(l+r)//2
                build(i<<1,l,m)
                build(i<<1|1,m+1,r)
                self.seg[i]=min(self.seg[i<<1],self.seg[i<<1|1])
            build(1,0,self.n-1)
        def push(self,i):
            if self.lazy[i]:
                v=self.lazy[i]
                self.seg[i<<1]+=v
                self.seg[i<<1|1]+=v
                self.lazy[i<<1]+=v
                self.lazy[i<<1|1]+=v
                self.lazy[i]=0
        def add(self,l,r,v):
            def upd(i,tl,tr):
                if r<tl or tr<l:return
                if l<=tl and tr<=r:
                    self.seg[i]+=v
                    self.lazy[i]+=v
                    return
                self.push(i)
                tm=(tl+tr)//2
                upd(i<<1,tl,tm)
                upd(i<<1|1,tm+1,tr)
                self.seg[i]=min(self.seg[i<<1],self.seg[i<<1|1])
            upd(1,0,self.n-1)

        def query(self,l,r):
            def qry(i,tl,tr):
                if r<tl or tr<l:return float('inf')
                if l<=tl and tr<=r:
                    return self.seg[i]
                self.push(i)
                tm=(tl+tr)//2
                return min(
                    qry(i<<1,tl,tm),
                    qry(i<<1|1,tm+1,tr)
                )
            return qry(1,0,self.n-1)
        def view(self):
            res=[0]*self.n
            def dfs(i,l,r):
                if l==r:
                    res[l]=self.seg[i]
                    return
                self.push(i)
                m=(l+r)//2
                dfs(i<<1,l,m)
                dfs(i<<1|1,m+1,r)
            dfs(1,0,self.n-1)
            return res
        
