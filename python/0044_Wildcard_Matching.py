# DP
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False

        n, m = len(s), len(p)
        # state
        dp = [[False] * (m + 1) for _ in range(2)]

        # initialization
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == "*"

        for i in range(1, n + 1):
            dp[i % 2][0] = False
            for j in range(1, m + 1):
                if p[j - 1] == "*":
                    dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[i % 2][j - 1]
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "?")

        return dp[n % 2][m]         
        
# Memoization        
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, 0, p, 0, {})

    def dfs(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty
        if len(s) == i:
            for index in range(j, len(p)):
                if p[index] != "*":
                    return False
            return True
        
        if len(p) == j:
            return False

        if p[j] == "*":
            result = self.dfs(s, i + 1, p, j, memo) or self.dfs(s, i, p, j + 1, memo)
        else:
            result = (s[i] == p[j] or p[j] == "?") and self.dfs(s, i + 1, p, j + 1, memo)
        
        memo[(i, j)] = result
        return result