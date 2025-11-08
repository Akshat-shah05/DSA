class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def backtrack(row, cols, diags, antidiags):
            nonlocal ans
            if row == n:
                ans += 1
            
            for col in range(n):
                diag = row + col
                antidiag = row - col
                if col in cols or diag in diags or antidiag in antidiags:
                    continue
                
                cols.add(col)
                diags.add(diag)
                antidiags.add(antidiag)

                backtrack(row + 1, cols, diags, antidiags)

                antidiags.remove(antidiag)
                diags.remove(diag)
                cols.remove(col)
        
        backtrack(0, set(), set(), set())
        return ans
