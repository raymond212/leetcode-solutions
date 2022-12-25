class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort() 
        
        a = 0 # Minimum candidate
        b = price[n - 1] - price[0] # Maximum candidate
        res = 0
        
        while a <= b:
            mid = (a + b) // 2
            if self.possible(price, k, mid):
                res = mid
                a = mid + 1
            else:
                b = mid - 1
        
        return res
        
    
    def possible(self, price, k, cand):
        count = 1
        last = price[0]
        i = 1

        while count < k and i < len(price):
            if price[i] - last >= cand:
                last = price[i]
                count += 1
            i += 1

        return count == k