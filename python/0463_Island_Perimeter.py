class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = neighbors = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                islands += 1
                if r + 1 < m and grid[r + 1][c] == 1:
                    neighbors += 1
                if c + 1 < n and grid[r][c + 1] == 1:
                    neighbors += 1
        return 4 * islands - 2 * neighbors