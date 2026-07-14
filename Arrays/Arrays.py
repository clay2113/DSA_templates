from bisect import bisect_left

#==================================================
#NittinS snippets
#
#SUBARRAY SUM TABLE
#
#Think:
#Need sum of every subarray
#
#Idea:
#Extend each start index
#
#Vars:
#n        -> array size
#dp[i][j] -> sum of arr[i...j]
#i        -> start index
#j        -> end index
#
#TC: O(n²)
#SC: O(n²)
#==================================================

def sub_sums(arr):
    #NittinS snippets
    n=len(arr)
    dp=[[0]*n for i in range(n)]

    for i in range(n):
        dp[i][i]=arr[i]

        for j in range(i+1,n):
            dp[i][j]=dp[i][j-1]+arr[j]

    return dp


#==================================================
#NittinS snippets
#
#NEXT PERMUTATION
#
#Think:
#Next lexicographical ordering
#
#Idea:
#Pivot -> Swap -> Reverse
#
#Vars:
#n      -> array length
#pivot  -> first decreasing index from right
#i      -> traversal index
#l,r    -> reverse pointers
#
#TC: O(n)
#SC: O(1)
#
#==================================================

def nextper(arr):
    #NittinS snippets
    n=len(arr)
    pivot=-1

    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break

    if pivot==-1:
        arr.reverse()
        return

    for i in range(n-1,pivot,-1):
        if arr[i]>arr[pivot]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break

    l,r=pivot+1,n-1

    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1


#==================================================
#NittinS snippets
#
#KADANE
#
#Think:
#Maximum contiguous subarray
#
#Idea:
#Negative prefix hurts future answer
#
#Vars:
#best -> best answer so far
#cur  -> current subarray sum
#x    -> current element
#
#TC: O(n)
#SC: O(1)
#
#==================================================

def max_sub(nums):
    #NittinS snippets
    best=cur=nums[0]

    for x in nums[1:]:
        cur=x if cur<0 else cur+x
        best=max(best,cur)

    return best



#==================================================
#NittinS snippets
#
#EXPAND AROUND CENTER
#
#Think:
#Generate all palindromic substrings
#
#Idea:
#Expand from every center
#Odd + Even centers
#
#Vars:
#n    -> string length
#pals -> palindrome intervals
#l,r  -> expansion pointers
#i    -> center index
#
#TC: O(n²)
#SC: O(n²)
#
#
#==================================================

def pal(s):
    #NittinS snippets
    n=len(s)
    pals=set()

    for i in range(n):
        l,r=i-1,i+1

        pals.add((i,i))

        while l>=0 and r<n:
            if s[l]!=s[r]:
                break

            pals.add((l,r))
            l-=1
            r+=1

    for i in range(n-1):
        if s[i]==s[i+1]:
            l=i-1
            r=i+2

            pals.add((i,i+1))

            while l>=0 and r<n:
                if s[l]!=s[r]:
                    break

                pals.add((l,r))
                l-=1
                r+=1

    return pals
