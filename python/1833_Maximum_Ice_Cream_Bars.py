class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        idx = 0
        while idx < len(costs) and costs[idx] <= coins:
            coins -= costs[idx]
            idx += 1
        return idx