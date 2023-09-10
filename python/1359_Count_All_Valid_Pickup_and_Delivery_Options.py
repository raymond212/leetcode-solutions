class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        mod = int(1e9 + 7)
        for i in range(2, n + 1):
            ans = ans * i * (2 * i - 1) % mod
        return ans