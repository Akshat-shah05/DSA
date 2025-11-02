class TrieNode:
    def __init__(self):
        self.children = {} # --> char -> TrieNode
        self.sentences = defaultdict(int) # --> Sentence -> count

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
        
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()

    def input(self, c: str) -> List[str]:
        if c == "#":
            full_sentence = "".join(self.curr_sentence)
            self.add_to_trie(full_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        if c not in self.curr_node.children:
            self.curr_sentence.append(c)
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        self.curr_sentence.append(c)
        sentences = [(val, key) for key, val in self.curr_node.sentences.items()]
        sentences.sort(key = lambda x: (-x[0], x[1]))
        ans = []
        for i in range(min(3, len(sentences))):
            ans.append(sentences[i][1])
        
        return ans

    def add_to_trie(self, sentence, count):
        root = self.root
        for c in sentence:
            if c not in root.children:
                root.children[c] = TrieNode()
            
            root = root.children[c]
            root.sentences[sentence] += count
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)