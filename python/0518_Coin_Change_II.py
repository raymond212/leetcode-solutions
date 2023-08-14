class Solution:
    def change(self, amount, coins) -> int:
        memo = {}
        coins.sort()

        def dfs(remain, start):
            key = (remain, start)
            if key in memo:
                return memo[key]
            if remain == 0:
                return 1
            ans = 0
            for i in range(start, len(coins)):
                if coins[i] > remain:
                    break
                ans += dfs(remain - coins[i], i)
            memo[key] = ans
            return ans

        return dfs(amount, 0)