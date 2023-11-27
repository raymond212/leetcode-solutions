class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        adj = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

        for i in range(1, n):
            arr = [0] * 10
            for j in range(10):
                for k in adj[j]:
                    arr[j] += dp[k]
            dp = arr
            
        return sum(dp) % (10 ** 9 + 7)