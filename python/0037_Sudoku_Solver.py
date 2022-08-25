class Solution:
    def solveSudoku(self, str_board: List[List[str]]) -> None:
        board = [[(0 if str_board[i][j] == "." else int(str_board[i][j])) for j in range(9)] for i in range(9)]
        used = self.initialize_used(board)
        self.dfs(board, 0, used)
        for i in range(9):
            for j in range(9):
                str_board[i][j] = str(board[i][j])
        return str_board
    
    def initialize_used(self, board):
        used = {
            "row": [set() for _ in range(9)],
            "col": [set() for _ in range(9)],
            "box": [set() for _ in range(9)]
        }
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == 0:
                    continue
                used["row"][i].add(val)
                used["col"][j].add(val)
                used["box"][i // 3 * 3 + j // 3].add(val)
        
        return used

    def dfs(self, board, index, used):
        if index == 81:
            return True
        
        i, j = index // 9, index % 9
        if board[i][j] != 0:
            return self.dfs(board, index + 1, used)
        
        for val in range(1, 10):
            if not self.is_valid(i, j, val, used):
                continue
            
            board[i][j] = val
            used["row"][i].add(val)
            used["col"][j].add(val)
            used["box"][i // 3 * 3 + j // 3].add(val)

            if self.dfs(board, index + 1, used):
                return True

            used["box"][i // 3 * 3 + j // 3].remove(val)   
            used["col"][j].remove(val)
            used["row"][i].remove(val)
            board[i][j] = 0
        
        return False

    def is_valid(self, i, j, val, used):
        if val in used["row"][i]:
            return False
        if val in used["col"][j]:
            return False
        if val in used["box"][i // 3 * 3 + j // 3]:
            return False
        return True