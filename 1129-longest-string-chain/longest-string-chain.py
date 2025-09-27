class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)

        dp = defaultdict(int)
        ans = 1
        for word in words:
            curr = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in dp:
                    curr = max(curr, dp[pred] + 1)
            
            dp[word] = curr
            ans = max(ans, curr)
    
        return ans
        
