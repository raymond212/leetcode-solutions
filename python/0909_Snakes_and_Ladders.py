class Solution:
    def snakesAndLadders(self, grid: List[List[int]]) -> int:
        n = len(grid)
        board = [-1] * (n * n)

        # initialize board
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                row = n - 1 - i
                col = 0
                if row % 2 == 0:
                    col = j + 1
                else:
                    col = n - j
                cur = row * n + col - 1
                board[cur] = grid[i][j] - 1
        
        # bfs
        q = deque([0])
        visited = {0}
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur == n * n - 1:
                    return steps
                for next_square in range(cur + 1, min(cur + 6, n * n - 1) + 1):
                    if board[next_square] > -1:
                        next_square = board[next_square]
                    if next_square in visited:
                        continue
                    q.append(next_square)
                    visited.add(next_square)
            steps += 1

        return -1
