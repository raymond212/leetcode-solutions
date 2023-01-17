class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        remaining_zeros = s.count("0")
        ans = remaining_zeros
        flips = 0 
        for i in range(n):
            if s[i] == "0":
                remaining_zeros -= 1
            else:
                flips += 1
            ans = min(ans, remaining_zeros + flips)
        return ans