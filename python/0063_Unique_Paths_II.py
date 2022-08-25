class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        memo = {}
        return self.dfs(0, 0, obstacle_grid, memo)
    
    def dfs(self, row, col, obstacle_grid, memo):
        if (row, col) in memo:
            return memo[(row, col)]
        if row == len(obstacle_grid) or col == len(obstacle_grid[0]) or obstacle_grid[row][col] == 1:
            return 0
        if row == len(obstacle_grid) - 1 and col == len(obstacle_grid[0]) - 1:
            return 1

        memo[(row, col)] = self.dfs(row, col + 1, obstacle_grid, memo) + self.dfs(row + 1, col, obstacle_grid, memo)
        return memo[(row, col)]