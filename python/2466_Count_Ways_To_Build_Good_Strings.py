# Bottom up DP
class Solution1:
    def countGoodStrings(self, low: int, high: int, num_zeros: int, num_ones: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * high

        for i in range(1, high + 1):
            if i >= num_zeros:
                dp[i] += dp[i - num_zeros]
            if i >= num_ones:
                dp[i] += dp[i - num_ones]
            dp[i] %= MOD
        
        return sum(dp[low : high + 1]) % MOD
        
# Top down DP
class Solution2:
    def countGoodStrings(self, low: int, high: int, num_zeros: int, num_ones: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [-1] * (high + 1)

        def dfs(l):
            if l > high:
                return 0
            if dp[l] != -1:
                return dp[l]

            ans = 0
            if l >= low:
                ans = 1
            ans = ans + dfs(l + num_zeros) + dfs(l + num_ones)

            dp[l] = ans % MOD
            return dp[l]

        return dfs(0)