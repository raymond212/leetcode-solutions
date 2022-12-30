class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n - 1] += 1
        
        for i in range(n - 1, 0, -1):
            if digits[i] >= 10:
                digits[i] -= 10
                digits[i - 1] += 1
            else:
                break

        if digits[0] >= 10:
            digits[0] -= 10
            digits.insert(0, 1)

        return digits