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
