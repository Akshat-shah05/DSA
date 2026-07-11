class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        if endWord not in wordSet:
            return 0

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            word_arr = [char for char in word]

            for i in range(len(word_arr)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    old = word_arr[i]
                    word_arr[i] = char

                    new_word = "".join(word_arr)
                    if new_word in wordSet:
                        q.append((new_word, steps + 1))
                        seen.add(new_word)
                        wordSet.remove(new_word)
                    
                    word_arr[i] = old
        return 0

