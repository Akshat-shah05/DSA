class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            correct = row[i + 1] == x + 1 if x % 2 == 0 else row[i + 1] == x - 1
            if correct: continue
            ans +=1
            for j in range(i + 1, len(row)):
                correct = row[j] == x + 1 if x % 2 == 0 else row[j] == x - 1
                if correct:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    break

        return ans