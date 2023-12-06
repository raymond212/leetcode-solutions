class Solution:
    def totalMoney(self, n: int) -> int:
        a, b = n // 7, n % 7
        return a * 28 + 7 * a * (a - 1) // 2 + b * (b + 1) // 2 + b * a