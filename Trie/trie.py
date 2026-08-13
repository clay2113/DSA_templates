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

class TrieNode:
    def __init__(self):
        self.next={}
        self.end=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,s):
        node=self.root
        for c in s:
            if c not in node.next:
                node.next[c]=TrieNode()
            node=node.next[c]
        node.end+=1

    def search(self,s):
        node=self.root
        for c in s:
            if c not in node.next:
                return False
            node=node.next[c]
        return node.end>0

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
