class Solution:
    def numSub(self, str: str) -> int:
        p1, p2 = 0, 0
        count = 0
        while p2 < len(str):
            if str[p1] != "1":
                p1 += 1
                p2 += 1
            else:
                while p2 < len(str) and str[p2] == "1":
                    p2 += 1
                dif = p2 - p1
                count += (dif * (dif + 1)) // 2
                p1 = p2
        return count % 1000000007