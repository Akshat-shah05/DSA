class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()

        for (sentence, count) in zip(sentences, times):
            self._add_to_trie(sentence, count)
        
        self.curSent = []
        self.curNode = self.root
        self.dead = TrieNode()

    def input(self, c: str) -> List[str]:
        if c == "#":
            curSentence = "".join(self.curSent)
            self._add_to_trie(curSentence, 1)
            self.curSent = []
            self.curNode = self.root
            return []
        
        self.curSent.append(c)
        if c not in self.curNode.children:
            self.curNode = self.dead
            return []
        
        self.curNode = self.curNode.children[c]
        sentences = self.curNode.sentences
        sorted_sentences = sorted(sentences.items(), key=lambda x: (-x[1], x[0]))

        ans = []

        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        
        return ans

    def _add_to_trie(self, sentence, count):
        root = self.root
        for ch in sentence:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
            root.sentences[sentence] += count
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)