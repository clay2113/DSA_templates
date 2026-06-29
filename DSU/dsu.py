#DISJOINT SET UNION MAIN

    class DSU:
    #NittinS snippets
        def __init__(self,n):
            self.parent=list(range(n))
            self.size=[1]*n
            self.components=n
        def find(self,x):
            if self.parent[x]!=x:
                self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
        def union(self,a,b):
            pa=self.find(a)
            pb=self.find(b)
            if pa==pb:
                return False
            if self.size[pa]<self.size[pb]:
                pa,pb=pb,pa
            self.parent[pb]=pa
            self.size[pa]+=self.size[pb]
            self.components-=1
            return True

  #DISJOINT SET UNION  WITH   COMPONENT SIZE TRACKER AND NO.OF GROUPS OF NODE OF SIZE K

    class DSU:
        # NittinS snippets
        def __init__(self, n,k=1):
            self.parent=list(range(n))
            self.size=[1]*n
            self.components = n
            self.cnt=Counter({1: n})
            self.ans=0
            self.k=k
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, a, b):
            pa = self.find(a)
            pb = self.find(b)
            if pa == pb:
                return False
            if self.size[pa] < self.size[pb]:
                pa, pb = pb, pa
            sa = self.size[pa]
            sb = self.size[pb]
            self.ans-=sa//self.k
            self.ans-=sb//self.k
            self.ans+=(sa+sb)//self.k
            self.cnt[sa] -= 1
            if self.cnt[sa] == 0:
                del self.cnt[sa]
            self.cnt[sb] -= 1
            if self.cnt[sb] == 0:
                del self.cnt[sb]
            self.parent[pb] = pa
            self.size[pa] += sb
            self.cnt[self.size[pa]] += 1
            self.components -= 1
            return True
        def len_comp(self):
            return self.components
        def count_size(self, k):
            return self.cnt[k]
