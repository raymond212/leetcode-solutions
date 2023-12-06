class Solution:
    def totalMoney(self, n: int) -> int:
        # sum of integers from 1 to x, inclusive
        def calc(x):
            return x * (x + 1) // 2

        a, b = n // 7, n % 7
        return a * 28 + 7 * calc(a - 1) + calc(b) + b * a