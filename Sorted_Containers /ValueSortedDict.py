# VALUE SORTED DICT
# NittinS Snippets
# ORDER : (value,key)
# SET/DEL/KTH/RANK : O(logN)
# GET/LEN            : O(1)

class ValueSortedDict:
    class Node:
        __slots__="key","val","pri","l","r","sz"
        def __init__(self,k,v):
            self.key=k; self.val=v
            self.pri=random.random()
            self.l=self.r=None; self.sz=1
    def __init__(self):
        self.root=None
        self.d={}
    def size(self,x):
        return x.sz if x else 0
    def upd(self,x):
        if x:x.sz=1+self.size(x.l)+self.size(x.r)
    def rotR(self,x):
        y=x.l; x.l=y.r; y.r=x
        self.upd(x); self.upd(y)
        return y
    def rotL(self,x):
        y=x.r; x.r=y.l; y.l=x
        self.upd(x); self.upd(y)
        return y
    def insert(self,x,y):
        if not x:return y
        if (y.val,y.key)<(x.val,x.key):
            x.l=self.insert(x.l,y)
            if x.l.pri<x.pri:x=self.rotR(x)
        else:
            x.r=self.insert(x.r,y)
            if x.r.pri<x.pri:x=self.rotL(x)
        self.upd(x)
        return x
    def merge(self,a,b):
        if not a:return b
        if not b:return a
        if a.pri<b.pri:
            a.r=self.merge(a.r,b)
            self.upd(a)
            return a
        else:
            b.l=self.merge(a,b.l)
            self.upd(b)
            return b
    def erase(self,x,k,v):
        if not x:return None
        if (v,k)<(x.val,x.key):
            x.l=self.erase(x.l,k,v)
        elif (v,k)>(x.val,x.key):
            x.r=self.erase(x.r,k,v)
        else:
            return self.merge(x.l,x.r)
        self.upd(x)
        return x
    def __setitem__(self,k,v):
        if k in self.d:
            self.root=self.erase(
                self.root,k,self.d[k]
            )
        self.d[k]=v
        self.root=self.insert(
            self.root,self.Node(k,v)
        )
    def __getitem__(self,k):
        return self.d[k]
    def get(self,k,default=None):
        return self.d.get(k,default)
    def __contains__(self,k):
        return k in self.d
    def __len__(self):
        return len(self.d)
    def __delitem__(self,k):
        self.root=self.erase(
            self.root,k,self.d[k]
        )
        del self.d[k]
    def min(self):
        if not self.root:raise KeyError
        x=self.root
        while x.l:x=x.l
        return x.key,x.val
    def max(self):
        if not self.root:raise KeyError
        x=self.root
        while x.r:x=x.r
        return x.key,x.val
    def kth(self,k):
        if k<0:k+=len(self)
        if not 0<=k<len(self):raise IndexError
        x=self.root
        while x:
            s=self.size(x.l)
            if k<s:
                x=x.l
            elif k==s:
                return x.key,x.val
            else:
                k-=s+1
                x=x.r 
    def rank(self,k):
        v=self.d[k]
        x=self.root
        ans=0
        while x:
            if (v,k)<=(x.val,x.key):
                x=x.l
            else:
                ans+=self.size(x.l)+1
                x=x.r
        return ans
    def items(self):
        st=[]; x=self.root
        while st or x:
            while x:
                st.append(x)
                x=x.l
            x=st.pop()
            yield x.key,x.val
            x=x.r
    def keys(self):
        for k,v in self.items():
            yield k
    def values(self):
        for k,v in self.items():
            yield v


### `__init__()`

Initializes the Treap root and the normal dictionary `key → value`.

### `Node()`

Creates one Treap node containing the key, value, random priority, children, and subtree size.

### `size(x)`

Returns the number of nodes in subtree `x`. Returns `0` for `None`.

### `upd(x)`

Recalculates `x.sz` from the sizes of its left and right subtrees.

### `rotR(x)`

Performs a right rotation to maintain the Treap's heap property.

### `rotL(x)`

Performs a left rotation to maintain the Treap's heap property.

### `insert(x, y)`

Inserts node `y` according to `(value, key)` ordering and restores the Treap priority property.

### `merge(a, b)`

Merges two Treaps where every element in `a` is smaller than every element in `b`.

### `erase(x, k, v)`

Removes `(value, key)` from the Treap and merges its two resulting subtrees.

### `__setitem__(k, v)`

Sets `d[k] = v`. If `k` already exists, removes its old value before inserting the new one.

### `__getitem__(k)`

Returns the value associated with `k` in **O(1)**.

### `get(k, default)`

Returns `d[k]` if present, otherwise returns `default`.

### `__contains__(k)`

Checks whether `k` exists in the dictionary.

### `__len__()`

Returns the number of key-value pairs in the structure.

### `__delitem__(k)`

Deletes key `k` from both the dictionary and the Treap.

### `min()`

Returns the `(key, value)` pair with the smallest `(value, key)`.

### `max()`

Returns the `(key, value)` pair with the largest `(value, key)`.

### `kth(k)`

Returns the **0-indexed k-th smallest** `(key, value)` using subtree sizes.

### `rank(k)`

Returns how many elements have `(value, key)` smaller than the specified key.

### `items()`

Iterates through all `(key, value)` pairs in increasing `(value, key)` order.

### `keys()`

Iterates through keys in increasing value order.

### `values()`

Iterates through values in increasing `(value, key)` order.
