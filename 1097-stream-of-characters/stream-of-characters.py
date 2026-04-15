class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # maps a character to a trie node
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.trie = TrieNode("*")
    
    def add_word(self, word: str):
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            
            cur = cur.children[char]
        
        cur.is_terminal = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.prefix_tree = Trie()
        for word in words:
            self.prefix_tree.add_word(word[::-1])
        
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        iterator = self.prefix_tree.trie
        for char in reversed(self.stream):
            if char not in iterator.children:
                return False

            iterator = iterator.children[char]
            if iterator.is_terminal:
                return True
        
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)