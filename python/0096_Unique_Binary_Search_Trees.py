class Solution:
    def numTrees(self, n: int) -> int:
        return self.dfs(n, {})
    
    def dfs(self, n, memo):
        if n == 0:
            return 1
        
        if n in memo:
            return memo[n]
        
        count = 0
        for i in range(1, n + 1):
            left = self.dfs(i - 1, memo)
            right = self.dfs(n - i, memo)
            count += left * right
        
        memo[n] = count
        return count
            