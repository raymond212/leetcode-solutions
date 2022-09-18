class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if self.validRow(board, i) and self.validCol(board, i):
                continue
            return False
        for i in range(3):
            for j in range(3):
                if self.validBox(board, i * 3, j * 3):
                    continue
                return False
        return True
    
    def validRow(self, board, row):
        appeared = set()
        for i in range(9):
            val = board[row][i]
            if val == ".":
                continue
            if val in appeared:
                return False
            appeared.add(val)
        return True

    def validCol(self, board, col):
        appeared = set()
        for i in range(9):
            val = board[i][col]
            if val == ".":
                continue
            if val in appeared:
                return False
            appeared.add(val)
        return True
    
    def validBox(self, board, x, y):
        appeared = set()
        for i in range(3):
            for j in range(3):
                val = board[x + i][y + j]
                if val == ".":
                    continue
                if val in appeared:
                    return False
                appeared.add(val)
        return True