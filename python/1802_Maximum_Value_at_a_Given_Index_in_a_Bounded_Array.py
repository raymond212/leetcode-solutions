class Solution:
    def maxValue(self, n: int, index: int, c: int) -> int:
        a = index
        b = n - index - 1
        a, b = max(a, b), min(a, b) # a >= b

        # both pyramid sides cut off
        k = (2 * c + a * (a + 1) + b * (b + 1)) // (2 * (1 + a + b))
        if k > a:
            return k
        
        # shorter pyramid side cut off
        k = floor((1 - 2 * b + sqrt((2 * b - 1) ** 2 - 4 * (2 * a + 2 - b * b - b - 2 * c))) / 2)
        if k > b:
            return k

        # perfect pyramid
        k = floor(1 + sqrt(c - a - b - 1))
        return k