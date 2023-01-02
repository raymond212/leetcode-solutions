DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        x, y = self.find(grid, 1)
        obstacle_count = self.countObstacles(grid)
        path_length = m * n - obstacle_count
        return self.dfs(grid, x, y, [(x, y)], {(x, y)}, path_length)

    def dfs(self, grid, x, y, path, visited, path_length):
        if grid[x][y] == 2:
            if len(path) == path_length:
                return 1
            return 0
        res = 0
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if self.isValid(nx, ny, grid) and grid[nx][ny] != -1 and (nx, ny) not in visited:
                path.append((nx, ny))
                visited.add((nx, ny))
                res += self.dfs(grid, nx, ny, path, visited, path_length)
                visited.remove((nx, ny))
                path.pop()
        return res

    def find(self, grid, target):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == target:
                    return (i, j)

    def countObstacles(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    count += 1
        return count

    def isValid(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])