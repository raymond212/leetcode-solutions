class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [0] * m
        ones_col = [0] * n

        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    ones_row[row] += 1
                    ones_col[col] += 1
        
        # Use ones_row[r] + zeros_row[r] = m and ones_col[c] + zeros_col[c] = n
        res = [[2 * ones_row[row] + 2 * ones_col[col] - m - n for col in range(n)] for row in range(m)]
        return res