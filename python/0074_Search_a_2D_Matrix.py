class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        start, end = 0, len(matrix) * len(matrix[0]) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            val = self.get(matrix, mid)
            if val == target:
                return True
            elif val < target:
                start = mid
            else:
                end = mid
            
        if self.get(matrix, start) == target or self.get(matrix, end) == target:
            return True
        return False

    def get(self, matrix, index):
        x = index // len(matrix[0])
        y = index % len(matrix[0])
        return matrix[x][y]