DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        human_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: # rotten orange
                    queue.append((i, j))
                if grid[i][j] == 1: # orange
                    human_count += 1

        day = 0
        if human_count == 0:
            return 0

        while queue:
            day += 1
            for i in range(len(queue)):
                zombie = queue.popleft()
                for delta_x, delta_y in DIRECTIONS:
                    next_x = zombie[0] + delta_x
                    next_y = zombie[1] + delta_y
                    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        queue.append((next_x, next_y))
                        human_count -= 1
            if human_count == 0:
                return day
        
        return -1