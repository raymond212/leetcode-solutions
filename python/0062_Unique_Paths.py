class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.dfs(0, 0, m, n, memo)
    
    def dfs(self, row, col, m, n, memo):
        if (row, col) in memo:
            return memo[(row, col)]
        if row == m - 1 and col == n - 1:
            return 1

        if row > m - 1 or col > n - 1:
            return 0

        memo[(row, col)] = self.dfs(row, col + 1, m, n, memo) + self.dfs(row + 1, col, m, n, memo)
        return memo[(row, col)]