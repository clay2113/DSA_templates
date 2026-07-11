#LONGEST CYCLE IN A DIRECTED GRAPH CONSISTING ONLY SINGLE CYCLE AT MOST FROM LC 2360
# time : O(N)
def long_cycle(edges):
        adj_list=defaultdict(lambda:set())
        check={}
        for i in edges:
              adj_list[i[1]].add(i[0])
              adj_list[i[0]].add(i[1])
              check[i]=edges[i]
        depth={}
        visited=set()
        rel={}
        def dfs(node,d):
            visited.add(node)
            depth[node]=d
            co=-1
            for i in adj_list[node]:
                if i not in visited: 
                    rel[node]=i
                    co=max(co,dfs(i,d+1))
                    del(rel[node])
                else:
                    if i in rel and rel[i]!=node:
                        co=max(co,d-depth[i]+1)
                    elif i in rel and rel[i]==node:
                        if i in check and node in check and check[i]==node and check[node]==i:
                            co=max(co,2)
            return co    
        max_val=-1 
        for i in range(len(edges)):
            if i not in visited:
                max_val=max(max_val,dfs(i,0))
        return max_val
