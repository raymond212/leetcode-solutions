# DP solution
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        ans = ""
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        maxLen = 1
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end + 1]

        return ans

# Two pointers
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

# First two pointers solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return ""

        length = 0
        index = 0
        for start in range(len(s)):
            cur_length = max(self.find_palindrome(s, start, start), self.find_palindrome(s, start, start + 1))
            if cur_length < length:
                continue

            index = start
            length = cur_length

        return s[index - (length - 1) // 2: index - (length - 1) // 2 + length]

    def find_palindrome(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1