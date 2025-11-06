class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([beginWord])
        steps = 1

        if beginWord == endWord:
            return 0
        
        if endWord not in wordSet:
            return 0

        while q:
            l = len(q)
            for _ in range(l):
                word = q.popleft()
                
                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + ch + word[i + 1:]
                        if newWord in wordSet:
                            q.append(newWord)
                            wordSet.remove(newWord)

            steps += 1
        
        return 0