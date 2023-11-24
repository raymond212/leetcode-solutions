class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        n = len(piles) // 3
        ans = 0

        for i in range(n, 3 * n, 2):
            ans += piles[i]

        return ans