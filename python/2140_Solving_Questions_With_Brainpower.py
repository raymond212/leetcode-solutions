class Solution1:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]
            
            dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]


class Solution2:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        def dfs(i):
            if i >= n:
                return 0
            if dp[i] > 0:
                return dp[i]
            points, skip = questions[i]

            dp[i] = max(dfs(i + 1), points + dfs(i + skip + 1))
            return dp[i]

        return dfs(0)
