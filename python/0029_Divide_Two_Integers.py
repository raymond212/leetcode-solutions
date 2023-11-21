class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Edge case
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1 

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        def helper(dividend, divisor):
            if dividend < divisor:
                return 0

            count = 1
            temp_div = divisor
            
            while (temp_div + temp_div) <= dividend:
                temp_div += temp_div
                count += count
            
            return count + helper(dividend - temp_div, divisor)

        return sign * helper(dividend, divisor)