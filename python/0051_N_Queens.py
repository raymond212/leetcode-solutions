class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]
        queens = []
        solutions = []
        self.dfs(0, n, board, queens, solutions)
        return solutions
        
    def dfs(self, row, n, board, queens, solutions):
        if row == n:
            solutions.append(list(board))
            return
        
        for col in range(n):
            if self.can_be_attacked(row, col, queens):
                continue
            old_str = board[row]
            new_str = old_str[0: col] + "Q" + old_str[col + 1:]
            board[row] = new_str
            queens.append((row, col))
            self.dfs(row + 1, n, board, queens, solutions)
            queens.pop()
            board[row] = old_str
    
    def can_be_attacked(self, row, col, queens):
        for q_row, q_col in queens:
            if q_col == col or abs(q_row - row) == abs(q_col - col):
                return True
        return False