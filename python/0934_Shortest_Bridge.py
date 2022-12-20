import collections

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def shortestBridge(self, grid) -> int:
        n = len(grid)
        q = collections.deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, q)
                    break
            if q:
                break

        while q:
            x, y, steps = q.popleft()
            for dx, dy in DIRS:
                x_, y_ = x + dx, y + dy
                if not self.isValid(grid, x_, y_) or grid[x_][y_] == -1:
                    continue
                if grid[x_][y_] == 1:
                    return steps
                grid[x_][y_] = -1
                q.append((x_, y_, steps + 1))

    def dfs(self, grid, x, y, q):
        if not self.isValid(grid, x, y) or grid[x][y] == -1:
            return
        if grid[x][y] == 0:
            q.append((x, y, 1))
        elif grid[x][y] == 1:
            grid[x][y] = -1
            for dx, dy in DIRS:
                self.dfs(grid, x + dx, y + dy, q)

    def isValid(self, grid, x, y):
        n = len(grid)
        return 0 <= x < n and 0 <= y < n