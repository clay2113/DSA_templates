#To get the number of divisible numbers <= mid with a  coins denominations which may 
#consist of primes and composite as well
#what i realised is that we can use lcm to handle that composite number errors and stuff 
#refer LC 3116
      def check(mid):
            inc=defaultdict(lambda:0)
            for i in range(1,1<<len(coins)):
                count=0
                curr_val=1
                for j in range(len(coins)):
                    if i&(1<<j)>0:
                        curr_val=lcm(curr_val,coins[j])
                        count+=1      
                inc[count]+=mid//curr_val
            ans=0
