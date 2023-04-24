class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
        MOD = 10 ** 9 + 7
        memo = {}

        def dfs(index, count, profit):
            if index == len(group):
                return profit >= minProfit

            key = (index, count, profit)
            if key in memo:
                return memo[key]

            # skip current crime
            ans = dfs(index + 1, count, profit)
            # commit current crime
            if count + group[index] <= n:
                ans += dfs(index + 1, count + group[index], min(minProfit, profit + profits[index]))

            memo[key] = ans % MOD
            return memo[key]

        return dfs(0, 0, 0)