#NUMBER OF WEAKLY CONNECTED COMPONENTS 
def countCC(g,n):
    adj=[[] for _ in range(n)]
    vis=[0]*n

    for u in range(n):
        for v in g[u]:
            adj[u].append(v)
            adj[v].append(u)

    def dfs(u):
        vis[u]=1
        for v in adj[u]:
            if not vis[v]: dfs(v)

    cnt=0
    for i in range(n):
        if not vis[i]:
            dfs(i)
            cnt+=1

    return cnt
