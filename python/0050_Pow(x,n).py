class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if n < 0:
            negative = True
            n = -n

        if n == 0:
            return 1
        
        product = self.myPow(x, n // 2)
        product *= product

        if n % 2 == 1:
            product *= x
        
        if negative:
            return 1 / product
            
        return product
