class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for c in range(n):
            ans += mat[c][c]
            r2 = n - c - 1
            if r2 != c:
                ans += mat[r2][c]
        return ans