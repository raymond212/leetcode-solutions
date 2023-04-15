class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n):
            for coins in range(k + 1):
                curSum = 0
                for cur_coins in range(min(coins, len(piles[i])) + 1):
                    if cur_coins > 0:
                        curSum += piles[i][cur_coins - 1]
                    dp[i + 1][coins] = max(dp[i + 1][coins], dp[i][coins - cur_coins] + curSum)
        return dp[n][k]