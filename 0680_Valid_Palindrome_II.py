class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s is None:
            return False

        left, right = self.find_difference(s, 0, len(s) - 1)

        if left >= right:
            return True

        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)

    def is_palindrome(self, s, left, right):
        left, right = self.find_difference(s, left, right)
        return left >= right

    def find_difference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right