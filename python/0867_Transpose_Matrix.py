class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[matrix[col][row] for col in range(m)] for row in range(n)]
        return res