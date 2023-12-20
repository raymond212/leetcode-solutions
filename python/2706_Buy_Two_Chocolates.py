class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = sorted(prices[:2])

        for i in range(2, len(prices)):
            x = prices[i]
            if x < min1:
                min1, min2 = x, min1
            elif x < min2:
                min2 = x
        
        price = min1 + min2
        return money if price > money else money - price
            