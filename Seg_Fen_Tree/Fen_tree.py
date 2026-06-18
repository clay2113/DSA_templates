#==================================================
#NittinS snippets
#
#FENWICK TREE (BIT)
#
#Think:
#Range sum queries
#Point updates
#
#Idea:
#Store partial sums using binary jumps
#Each index contributes to multiple ranges
#
#Vars:
#n        -> array length
#idx      -> current index
#delta    -> value to add
#left     -> range start
#right    -> range end
#
#TC:
#Build      -> O(nlogn) using add()
#Point Add  -> O(logn)
#Prefix Sum -> O(logn)
#Range Sum  -> O(logn)
#
#SC: O(n)
#
#Need:
#0-indexed externally
#Internally converted to 1-indexed
#Range query is inclusive [l,r]
#
#Notes:
#Smaller and simpler than segment tree
#Use for sums, frequencies, inversions
#
#==================================================

class FenwickTree:
    #NittinS snippets

    def __init__(self,n):
        self.n=n
        self.bit=[0]*(n+1)

    def add(self,idx,delta):
        idx+=1

        while idx<=self.n:
            self.bit[idx]+=delta
            idx+=idx&-idx

    def prefix_sum(self,idx):
        idx+=1
        s=0

        while idx>0:
            s+=self.bit[idx]
            idx-=idx&-idx

        return s

    def range_sum(self,left,right):
        return self.prefix_sum(right)-(
            self.prefix_sum(left-1) if left>0 else 0
        )
