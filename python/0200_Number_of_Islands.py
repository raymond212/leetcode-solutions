DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                count += 1
                self.remove_island(grid, i, j)
        
        return count
                
    def remove_island(self, grid, x, y):
        queue = collections.deque([[x, y]])
        grid[x][y] = "0"
        while queue:
            position = queue.popleft()
            for DIR in DIRS:
                next_x = position[0] + DIR[0]
                next_y = position[1] + DIR[1]
                if len(grid) > next_x >= 0 and len(grid[0]) > next_y >= 0 and grid[next_x][next_y] == "1":
                    queue.append([next_x, next_y])
                    grid[next_x][next_y] = "0"
