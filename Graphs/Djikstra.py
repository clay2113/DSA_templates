#Djikstra algorithm with edges as [x,y,w] and returns a DP 
      def djik(n,edges):
        dp=[float("inf") for i in range(n)]
        dp[0]=0
        adj_list=defaultdict(lambda:[])
        for i in edges:
            adj_list[i[0]].append((i[1],i[2]))
            adj_list[i[1]].append((i[0],i[2]))
        queue=SortedList([(0,0)])
        visited=set()
        while len(queue)!=0:
            ele=queue[0]
            queue.remove(queue[0])
            visited.add(ele[1])
            if len(visited)==n:
                break
            for i in adj_list[ele[1]]:
                if i[0] not in visited:
                    dp[i[0]]=min(dp[i[0]],ele[0]+i[1])
                    queue.add((ele[0]+i[1],i[0]))
        return dp
