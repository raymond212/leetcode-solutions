class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        profit = 0
        min = float('inf')
        n = len(prices)

        for price in prices:
            if price < min:
                min = price
            if price - min > profit:
                profit = price - min
        
        return profit