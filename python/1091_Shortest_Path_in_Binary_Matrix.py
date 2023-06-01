class Solution:    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        
        q = deque([(0, 0)])
        steps = 1
        
        while q:
            k = len(q)
            for _ in range(k):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return steps
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 1
            steps += 1
        
        return -1