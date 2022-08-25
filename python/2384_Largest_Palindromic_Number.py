class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for s in num:
            freq[ord(s) - ord('0')] += 1
        res = []
        mid = -1
        for i in range(9, -1, -1):
            if len(res) == 0 and i == 0:
                if mid == -1 and freq[0] > 0:
                    mid = 0
                continue
            for j in range(freq[i] // 2):
                res.append(i)
            if freq[i] % 2 == 1 and mid == -1:
                mid = i
        if mid != -1:
            res.append(mid)
            for i in range(len(res) - 2, -1, -1):
                res.append(res[i])
        else:
            for i in range(len(res) - 1, -1, -1):
                res.append(res[i])
        return "".join([str(x) for x in res])