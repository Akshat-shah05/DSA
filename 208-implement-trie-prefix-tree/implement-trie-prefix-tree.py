class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curNode = self.root
        
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            
            curNode = curNode.children[char]

        curNode.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.endOfWord
            
            char = word[index]
            if char not in node.children:
                return False

            return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)        

    def startsWith(self, prefix: str) -> bool:
        def dfs(node, index):
            if index == len(prefix):
                return True
            
            char = prefix[index]
            if char not in node.children:
                return False

            return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)     
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)