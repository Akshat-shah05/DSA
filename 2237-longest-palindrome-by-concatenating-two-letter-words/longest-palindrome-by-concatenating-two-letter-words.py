class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = defaultdict(int)
        pairs = 0
        centre = 0
        for word in words:
            if freq[word[::-1]] > 0:
                freq[word[::-1]] -= 1
                pairs += 1
            else:
                freq[word] += 1
        
        for word, count in freq.items():
            if word[0] == word[1]:
                pairs += count//2
                if count % 2 == 1:
                    centre = 1
        
        return pairs * 4 + centre * 2
