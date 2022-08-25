# Rabin Karp
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        BASE = 1000000

        if haystack is None or needle is None:
            return -1

        n = len(needle)
        if n == 0:
            return 0

        power = 1
        for i in range(n):
            power = (power * 31) % BASE

        needleCode = 0
        for i in range(n):
            needleCode = (needleCode * 31 + ord(needle[i])) % BASE

        hashCode = 0
        for i in range(len(haystack)):
            hashCode = (hashCode * 31 + ord(haystack[i])) % BASE
            if i < n - 1:
                continue

            if i >= n:
                hashCode = hashCode - (ord(haystack[i - n]) * power) % BASE
                hashCode %= BASE

            if hashCode == needleCode and haystack[i - n + 1:i + 1] == needle:
                return i - n + 1

        return -1

# O(n^2) solution
# class Solution:
#         def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0

#         for i in range(len(haystack) - len(needle) + 1):
#             for j in range(len(needle)):
#                 if haystack[i + j] != needle[j]:
#                     break
#             else:
#                 return i

#         return -1