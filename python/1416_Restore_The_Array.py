class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)
        n = len(str(k))
        dp = [0] * (m + 1)
        MOD = 10 ** 9 + 7

        def dfs(start):
            if dp[start]:
                return dp[start]

            if start == m:
                return 1
            if s[start] == '0':
                return 0

            count = 0
            for end in range(start, m):
                cur_num = s[start: end + 1]
                if int(cur_num) > k:
                    break
                count += dfs(end + 1)

            dp[start] = count % MOD
            return dp[start]

        return dfs(0)