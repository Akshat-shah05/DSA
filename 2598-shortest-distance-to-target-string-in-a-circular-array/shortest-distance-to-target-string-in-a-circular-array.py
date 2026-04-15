class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        l, r = startIndex, startIndex
        n = len(words)
        steps = 0
        while steps <= n:
            if words[l] == target or words[r] == target:
                return steps
            l = (l - 1 + n) % n
            r = (r + 1) % n
            steps += 1
        
        return -1
