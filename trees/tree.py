"""BINARY LIFTING + LCA"""
# KTH ANCESTOR + LOWEST COMMON ANCESTOR

# Build: O(NlogN)
# Kth Ancestor: O(logN)
# LCA Query: O(logN)
# Memory: O(NlogN)

class Bin_lift:
    #NittinS snippets
    def __init__(self,n,g,root=0):
        self.n=n
        self.LOG=n.bit_length()
        self.depth=[0]*n
        self.up=[[-1]*self.LOG for _ in range(n)]

        def dfs(v,p):
            self.up[v][0]=p
            for j in range(1,self.LOG):
                if self.up[v][j-1]!=-1:
                    self.up[v][j]=self.up[self.up[v][j-1]][j-1]
            for to in g[v]:
                if to!=p:
                    self.depth[to]=self.depth[v]+1
                    dfs(to,v)
        dfs(root,-1)

    def kth_ancestor(self,v,k):
        for j in range(self.LOG):
            if v==-1:return -1
            if k>>j&1:v=self.up[v][j]
        return v

    def lca(self,u,v):
        if self.depth[u]<self.depth[v]:
            u,v=v,u
        u=self.kth_ancestor(u,self.depth[u]-self.depth[v])
        if u==v:return u
        for j in range(self.LOG-1,-1,-1):
            if self.up[u][j]!=self.up[v][j]:
                u=self.up[u][j]
                v=self.up[v][j]
        return self.up[u][0]

    def dist(self,u,v):
        w=self.lca(u,v)
        return self.depth[u]+self.depth[v]-2*self.depth[w]
