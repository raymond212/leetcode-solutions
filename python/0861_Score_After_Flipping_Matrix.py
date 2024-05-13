class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for c in range(n):
            cnt_ones = 0
            for r in range(m):
                cnt_ones += grid[r][0] == grid[r][c]
            ans = 2 * ans + max(cnt_ones, m - cnt_ones)
        return ans