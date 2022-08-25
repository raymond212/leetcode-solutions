class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return ""

        letter_count = [0 for _ in range(128)]
        for i in range(len(s)):
            letter_count[ord(s[i])] += 1

        res = 0
        extra = False
        for i in range(len(letter_count)):
            res += letter_count[i] - (letter_count[i] % 2)
            if not extra and letter_count[i] % 2 == 1:
                res += 1
                extra = True

        return res