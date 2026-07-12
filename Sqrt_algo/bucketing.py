LC 2158. Amount of New Area Painted Each Day
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n=0
        for i in paint:
            n=max(n,i[1]+1)
        bucket=[[0,[0 for j in range(floor(sqrt(n)))],0] for i in range(ceil(sqrt(n))+1)]
        buc_len=floor(sqrt(n))
        ans=[]
        for i in paint:
            i[1]-=1
            if i[0]//buc_len==i[1]//buc_len:
                count=0
                if bucket[i[0]//buc_len][0]==1:
                    ans.append(0)
                else:
                    for j in range(i[0]%buc_len,i[1]%buc_len+1):
                        if bucket[i[0]//buc_len][1][j]==0:
                            count+=1
                            bucket[i[0]//buc_len][1][j]=1
                            bucket[i[0]//buc_len][2]+=1
                    ans.append(count)
            else:
                count=0
                for j in range(buc_len-1,i[0]%buc_len-1,-1):
                    if bucket[i[0]//buc_len][0]==0 and bucket[i[0]//buc_len][1][j]==0:
                        count+=1
                        bucket[i[0]//buc_len][1][j]=1
                        bucket[i[0]//buc_len][2]+=1
                for j in range(i[1]%buc_len+1):
                    if bucket[i[1]//buc_len][0]==0 and bucket[i[1]//buc_len][1][j]==0:
                        count+=1
                        bucket[i[1]//buc_len][1][j]=1 
                        bucket[i[1]//buc_len][2]+=1    
                for j in range(i[0]//buc_len+1,i[1]//buc_len):
                    if bucket[j][0]==0:
                        count+=buc_len-bucket[j][2]
                        bucket[j][0]+=1             
                ans.append(count)           
        return ans
