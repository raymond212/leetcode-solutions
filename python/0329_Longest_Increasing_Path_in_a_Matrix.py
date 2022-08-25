DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        dict = {}
        nums = []
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)] # dp[i][j] represents the length of the LICS ending at i, j

        for i in range(m):
            for j in range(n):
                if matrix[i][j] in dict:
                    dict[matrix[i][j]].append((i, j))
                else:
                    nums.append(matrix[i][j])
                    dict[matrix[i][j]] = [(i, j)]
        
        nums.sort()

        result = 0
        for num in nums: # start from the smallest number
            for i, j in dict[num]:
                maximum = 0
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] < num:
                        maximum = max(maximum, dp[x][y])
                dp[i][j] = maximum + 1
                result = max(result, dp[i][j])
        
        return result