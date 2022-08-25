DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def slidingPuzzle(self, init_state: List[List[int]]) -> int:
        final_state = [[1,2,3],[4,5,0]]
        if self.is_equal(init_state, final_state):
            return 0

        zero_pos = (0, 0)
        for i in range(2):
            for j in range(3):
                if init_state[i][j] == 0:
                    zero_pos = (i, j)        

        queue = collections.deque([[init_state, zero_pos]])
        visited = {self.hash_board(init_state)}
        steps = 1

        while queue:
            for _ in range(len(queue)):
                popped = queue.popleft()
                board = popped[0]
                z_x, z_y = popped[1][0], popped[1][1]
                for dx, dy in DIRECTIONS:
                    x, y = z_x + dx, z_y + dy
                    if 0 <= x < 2 and 0 <= y < 3:
                        board_copy = [row[:] for row in board]
                        board_copy[z_x][z_y] = board_copy[x][y]
                        board_copy[x][y] = 0
                        hashed = self.hash_board(board_copy)
                        if hashed in visited:
                            continue
                        if self.is_equal(board_copy, final_state):
                            return steps
                        visited.add(hashed)
                        queue.append([board_copy, (x, y)])
            steps += 1
        return -1          

    def is_equal(self, board1, board2):
        for i in range(2):
            for j in range(3):
                if board1[i][j] != board2[i][j]:
                    return False
        return True

    def hash_board(self, board):
        base = 1
        result = 0
        for i in range(2):
            for j in range(3):
                result += board[i][j] * base
                base *= 6
        return result