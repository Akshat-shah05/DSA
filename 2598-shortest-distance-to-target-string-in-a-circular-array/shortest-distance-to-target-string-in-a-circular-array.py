class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        l, r = startIndex, startIndex
        n = len(words)
        steps = 0
        while words[l] != target and words[r] != target and not (steps > 0 and l == r):
            l = (l - 1 + n) % n
            r = (r + 1) % n
            steps += 1
        
        if words[l] == target or words[r] == target:
            return steps
        
        return -1
