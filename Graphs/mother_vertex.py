def canReachAll(g,n):
    vis=[0]*n
    last=0
    def dfs(u):
        vis[u]=1
        for v in g[u]:
            if not vis[v]: dfs(v)
    for i in range(n):
        if not vis[i]:
            dfs(i)
            last=i
    vis=[0]*n
    dfs(last)
    return sum(vis)==n
#This is the mother vertex technique: a mother vertex is a vertex that can reach every other vertex. The algorithm runs in 
O(V+E)
