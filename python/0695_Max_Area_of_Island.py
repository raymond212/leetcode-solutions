class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def isIsland(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] == 1

        def dfs(r, c):
            if not isIsland(r, c) or visited[r][c]:
                return 0
            visited[r][c] = True
            ans = 1
            ans += dfs(r + 1, c)
            ans += dfs(r - 1, c)
            ans += dfs(r, c + 1)
            ans += dfs(r, c - 1)
            return ans

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans