# TRIE
# NittinS Snippets
# INSERT : O(L)
# SEARCH : O(L)
# PREFIX : O(L)
# DELETE : O(L)

# TRIE
# NittinS Snippets
# INSERT : O(L)
# SEARCH : O(L)
# PREFIX : O(L)
# DELETE : O(L)


#refer 421. Maximum XOR of Two Numbers in an Array
#it utilizes the fact that numbers can be like 30bits for 10**9 so O(bit_count()) query suffices for checking 
#maximum matching of the ideal number to be XORed ;)
class Trie:
  #NittinS Snippets
        class TrieNode:
            def __init__(self):
                self.next={}
                self.end=0
        def __init__(self):
            self.root=self.TrieNode()

        def insert(self,s):
            node=self.root
            for c in s:
                if c not in node.next:
                    node.next[c]=self.TrieNode()
                node=node.next[c]
            node.end=s

        def search(self,s):
            node=self.root
            for c in s:
                if c in node.next:
                    node=node.next[c]   
                elif str((int(c)+1)%2) in node.next:
                    node=node.next[str((int(c)+1)%2)]
                else:
                    return False
            return int(node.end,2)

        def startsWith(self,p):
            node=self.root
            for c in p:
                if c not in node.next:
                    return False
                node=node.next[c]
            return True

        def count(self,s):
            node=self.root
            for c in s:
                if c not in node.next:
                    return 0
                node=node.next[c]
            return node.end

        def delete(self,s):
            def dfs(node,i):
                if i==len(s):
                    if node.end==0:
                        return False
                    node.end-=1
                    return len(node.next)==0 and node.end==0
                c=s[i]
                if c not in node.next:
                    return False
                child=node.next[c]
                remove=dfs(child,i+1)
                if remove:
                    del node.next[c]
                return len(node.next)==0 and node.end==0
            dfs(self.root,0)



#another implementation 
class Trie:
    #NittinS snippets
    def __init__(self,B=31):
        self.B=B
        self.trie=[[-1,-1]]
        self.cnt=[0]

    def add(self,x):
        i=0
        self.cnt[i]+=1
        for b in range(self.B,-1,-1):
            bit=(x>>b)&1
            if self.trie[i][bit]==-1:
                self.trie[i][bit]=len(self.trie)
                self.trie.append([-1,-1])
                self.cnt.append(0)
            i=self.trie[i][bit]
            self.cnt[i]+=1

    def delete(self,x):
        i=0
        path=[]
        for b in range(self.B,-1,-1):
            bit=(x>>b)&1
            j=self.trie[i][bit]
            if j==-1 or self.cnt[j]==0:
                return False
            path.append((i,bit,j))
            i=j
        self.cnt[0]-=1
        for _,_,j in path:
            self.cnt[j]-=1
        return True

    def query(self,x):
        if self.cnt[0]==0:
            return None
        i=0
        y=0
        for b in range(self.B,-1,-1):
            bit=(x>>b)&1
            want=bit^1
            j=self.trie[i][want]
            if j!=-1 and self.cnt[j]>0:
                y|=want<<b
                i=j
            else:
                y|=bit<<b
                i=self.trie[i][bit]
        return x^y,y
