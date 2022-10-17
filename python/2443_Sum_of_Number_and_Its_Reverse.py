class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for val in range(num + 1):
            if int(str(val)[::-1]) + val == num:
                return True
        return False