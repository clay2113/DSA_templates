#CHECK BIPARTITE GRAPH OR NOT BY BFS AND 2 COLOR PROBLEM      ---   FOR DISCONNECTED COMPONENTS ALSO


	def bipar(edges,n):
	    #NittinS snippets 
		adj_list=defaultdict(lambda:[])
        for i in edges:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])   
        def bfs(root):
            #NittinS snippets
            q=deque([root,"a"])
            visited={}
            curr=1
            while len(q)!=0:
                ele=q.popleft()
                if ele=="a":
                    if len(q)==0:
                        break
                    curr+=1
                    q.append("a")
                else:
                    visited[ele]=curr&1
                    main.add(ele)
                    for i in adj_list[ele]:
                        if i in visited:
                            if visited[i]==visited[ele]:
                                return False
                        else:
                            q.append(i)
            return True              
        main=set()
        check=True
        for i in range(1,n+1):
            if i not in main:
                check=check and bfs(i)
        return check
