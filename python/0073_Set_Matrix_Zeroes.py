class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row = False
        first_col = False
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row = True
                    if c == 0:
                        first_col = True
                    if r > 0 and c > 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0
        if first_row:
            for c in range(n):
                matrix[0][c] = 0
        if first_col:
            for r in range(m):
                matrix[r][0] = 0
        return

