#TO FIND THE NUMBER OF STRONGLY CONNECTED COMPONENTS IN A DIRECTED GRAPH
def countSCC(g,n):
    rg=[[] for _ in range(n)]
    vis=[0]*n
    order=[]

    for u in range(n):
        for v in g[u]:
            rg[v].append(u)

    def dfs(u):
        vis[u]=1
        for v in g[u]:
            if not vis[v]: dfs(v)
        order.append(u)

    def dfs2(u):
        vis[u]=1
        for v in rg[u]:
            if not vis[v]: dfs2(v)

    for i in range(n):
        if not vis[i]: dfs(i)

    vis=[0]*n
    cnt=0

    for u in order[::-1]:
        if not vis[u]:
            dfs2(u)
            cnt+=1

    return cnt
