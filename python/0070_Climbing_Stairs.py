class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        return self.dfs(0, n, {})

    def dfs(self, step, n, memo):
        if step in memo:
            return memo[step]
        if step > n:
            return 0
        if step == n:
            return 1
        memo[step] = self.dfs(step + 1, n, memo) + self.dfs(step + 2, n, memo)
        return memo[step]