#TOPOLOGICAL SORT FROM ADJACENCY LIST
def topoSort(n,adj):
    indeg=[0]*n
    for u in range(n):
        for v in adj[u]:indeg[v]+=1
    q=deque(i for i in range(n) if indeg[i]==0)
    topo=[]
    while q:
        u=q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return topo if len(topo)==n else []
