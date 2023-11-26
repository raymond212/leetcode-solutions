class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        arr = [[0] * n for _ in range(m)]
        ans = 0

        for c in range(n):
            count = 0
            for r in range(m):
                if matrix[r][c]:
                    count += 1
                else:
                    count = 0
                arr[r][c] = count

        for r in range(m):
            arr[r].sort(reverse=True)
            for c in range(n):
                ans = max(ans, (c + 1) * arr[r][c])
                if n * arr[r][c] < ans:
                    break

        return ans