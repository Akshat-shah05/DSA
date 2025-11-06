class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {v : i for i, v in enumerate(row)}
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            correct = row[i + 1] == x ^ 1
            if correct: continue

            ans += 1
            partnerIdx = pos[x ^ 1]
            movedVal = row[i + 1]

            row[i + 1], row[partnerIdx] = row[partnerIdx], row[i + 1]
            pos[x ^ 1] = i + 1
            pos[movedVal] = partnerIdx

        return ans