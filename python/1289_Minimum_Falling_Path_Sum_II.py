class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[grid[i][j] for j in range(n)] for i in range(n)]

        for i in range(1, n):
            minVal, minIndex = self.findMinExcluding(dp, i - 1, -1)
            minVal2, _ = self.findMinExcluding(dp, i - 1, minIndex)
            for j in range(n):
                if j == minIndex:
                    dp[i][j] += minVal2
                else:
                    dp[i][j] += minVal
        
        return min(dp[n - 1])

    def findMinExcluding(self, grid, row, exclude):
        minVal, minIndex = float('inf'), 0
        for i in range(len(grid[row])):
            if i != exclude and grid[row][i] < minVal:
                minVal = grid[row][i]
                minIndex = i
        return minVal, minIndex
