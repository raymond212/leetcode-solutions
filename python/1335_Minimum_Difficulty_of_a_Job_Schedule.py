class Solution:
    def minDifficulty(self, cost: List[int], d: int) -> int:
        n = len(cost)

        if n < d:
            return -1

        @lru_cache(None)
        def dfs(day, start):
            maxd = 0
            ans = float('inf')
            
            for i in range(start, n - (d - day)):
                maxd = max(maxd, cost[i])
                if day != d:
                    ans = min(ans, maxd + dfs(day + 1, i + 1))
            
            if day == d:
                ans = maxd

            return ans
        
        return dfs(1, 0)
