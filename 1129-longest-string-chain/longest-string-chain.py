class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        longestSequence = 1

        for word in words:
            currLen = 1

            for i in range(len(word)):
                predecessor = word[0:i] + word[i + 1:len(word) + 1]

                if predecessor in dp:
                    prevLength = dp[predecessor]
                    currLen = max(currLen, prevLength + 1)
                
            dp[word] = currLen
            longestSequence = max(longestSequence, currLen)
        
        return longestSequence
