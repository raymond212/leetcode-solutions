class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        x, y = n - 1, 0
        count = 0
        while x >= 0 and y < m:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1

        return False