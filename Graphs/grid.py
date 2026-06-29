#NEIGHBOURS IN GRID RETURN AS VALID INDICES
        def neigh(i,j):
            m,n=len(grid),len(grid[0])
            c=[]
            if i+1<m:
                c.append((i+1,j))
            if j+1<n:
                c.append((i,j+1))
            if i-1>=0:
                c.append((i-1,j))
            if j-1>=0:
                c.append((i,j-1)) 
            return c
