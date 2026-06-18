#==================================================
#NittinS snippets
#
#BINARY SEARCH (EXACT)
#
#Think:
#Need exact value
#
#Idea:
#Discard half of search space each step
#
#Vars:
#lo,hi -> search range
#mid   -> middle value
#
#TC: O(logn)
#SC: O(1)
#
#Need:
#Search space must be sorted
#
#Notes:
#Returns insertion position if target not found
#
#==================================================

def bs(lo,hi):
    #NittinS snippets
    while lo<=hi:
        mid=(lo+hi)//2

        if check(mid):
            hi=mid-1
        else:
            lo=mid+1

    return lo


#==================================================
#NittinS snippets
#
#FIRST TRUE
#
#Think:
#Monotonic predicate
#FFFFTTTT
#
#Idea:
#Keep first valid answer
#
#Vars:
#lo,hi -> search range
#mid   -> middle value
#
#TC: O(logn)
#SC: O(1)
#
#Need:
#Predicate must be monotonic
#
#Pattern:
#FFFFTTTT
#     ^
#     answer
#
#Notes:
#Most common LC binary search template
#Used in Binary Search on Answer
#
#==================================================

def first_true(lo,hi):
    #NittinS snippets
    while lo<hi:
        mid=(lo+hi)//2

        if check(mid):
            hi=mid
        else:
            lo=mid+1

    return lo


#==================================================
#NittinS snippets
#
#LAST TRUE
#
#Think:
#Monotonic predicate
#TTTTFFFF
#
#Idea:
#Keep last valid answer
#
#Vars:
#lo,hi -> search range
#mid   -> middle value
#
#TC: O(logn)
#SC: O(1)
#
#Need:
#Predicate must be monotonic
#
#Pattern:
#TTTTFFFF
#   ^
# answer
#
#Notes:
#Use upper mid
#mid=(lo+hi+1)//2
#
#==================================================

def last_true(lo,hi):
    #NittinS snippets
    while lo<hi:
        mid=(lo+hi+1)//2

        if check(mid):
            lo=mid
        else:
            hi=mid-1

    return lo
