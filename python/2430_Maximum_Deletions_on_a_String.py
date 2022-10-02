class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        memo = {}
        return self.dfs(0, s, memo)
        
    def dfs(self, i, s, memo): # returns max number of deletions to delete s starting from index i
        n = len(s)
        if i == n:
            return 0
        if i in memo:
            return memo[i]
        res = 1
        # for j in range(1, (n - i) // 2 + 1):
        for j in range((n - i) // 2, 0, -1):
            if s[i: i + j] == s[i + j: i + 2 * j]:
                res = max(res, 1 + self.dfs(i + j, s, memo))
        memo[i] = res
        return memo[i]