class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        dp = {}
        ans = 1

        for word in words:
            wordChain = 1

            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in dp:
                    wordChain = max(wordChain, dp[pred] + 1)
            
            dp[word] = wordChain
            ans = max(ans, wordChain)
        
        return ans



