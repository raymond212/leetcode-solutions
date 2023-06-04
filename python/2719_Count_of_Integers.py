class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        n = len(num2)
        num1 = '0' * (n - len(num1)) + num1

        memo = {}
        mod = 10 ** 9 + 7

        def dfs(idx, cur_sum, equal_last_lower, equal_last_upper):
            if idx == n:
                if cur_sum >= min_sum:
                    return 1
                return 0

            key = (idx, cur_sum, equal_last_lower, equal_last_upper)
            if key in memo:
                return memo[key]

            ans = 0

            lower = int(num1[idx]) if equal_last_lower else 0
            upper = int(num2[idx]) if equal_last_upper else 9

            for i in range(lower, upper + 1):
                new_sum = cur_sum + i
                if new_sum <= max_sum:
                    ans += dfs(idx + 1, new_sum, equal_last_lower and i == lower, equal_last_upper and i == upper)

            memo[key] = ans % mod
            return memo[key]

        return dfs(0, 0, True, True)