class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            
            root = root.children[char]
        
        root.EOW = True


    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.EOW
            
            char = word[idx]
            if char not in node.children:
                return False
            
            return dfs(node.children[char], idx + 1)

        return dfs(self.root, 0)

    def startsWith(self, prefix: str) -> bool:
        def dfs(node, idx):
            if idx == len(prefix):
                return True
            
            char = prefix[idx]
            if char not in node.children:
                return False
            
            return dfs(node.children[char], idx + 1)

        return dfs(self.root, 0)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

