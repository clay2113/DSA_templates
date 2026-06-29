#BFS level ORDER TRAVERSAL O(N)
        def bfs(root):
            #NittinS snippets
            if root==None:
                return None
            q=deque([root,"a"])
            ans=[]
            curr=[]
            while len(q)!=0:
                ele=q.popleft()
                if ele=="a":
                    ans.append(curr)
                    if len(q)==0:
                        break
                    curr=[]
                    q.append("a")
                else:
                    curr.append(ele.val)
                    if ele.left != None:
                        q.append(ele.left)
                    if ele.right != None:
                        q.append(ele.right)           
            return ans
