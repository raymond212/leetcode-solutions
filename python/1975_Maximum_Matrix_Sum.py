class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = 0
        num_neg = 0
        min_abs = float('inf')
        for r in range(n):
            for c in range(n):
                x = matrix[r][c]
                res += abs(x)
                min_abs = min(min_abs, abs(x))
                if x <= 0:
                    num_neg += 1
        if num_neg % 2 == 1:
            res -= 2 * min_abs
        return res