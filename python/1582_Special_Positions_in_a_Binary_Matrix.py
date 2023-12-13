class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_freq = [0] * m
        col_freq = [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    row_freq[i] += 1
                    col_freq[j] += 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and row_freq[i] == 1 and col_freq[j] == 1:
                    res += 1
        
        return res