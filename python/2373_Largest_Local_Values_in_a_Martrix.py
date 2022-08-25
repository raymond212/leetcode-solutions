class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid:
            return []
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = self.get_max(grid, i, j)
        
        return res
    
    def get_max(self, grid, i, j):
        res = 0
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                res = max(res, grid[x][y])
        return res