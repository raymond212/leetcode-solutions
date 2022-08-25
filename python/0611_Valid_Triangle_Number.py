class Solution:
    def triangleNumber(self, s: List[int]) -> int:
        if not s or len(s) < 3:
            return 0

        s.sort()
        
        count = 0
        for large in range(len(s) - 1, 1, -1):
            small, mid = 0, large - 1
            while small < mid:
                if s[mid] + s[small] > s[large]:
                    count += mid - small
                    mid -= 1
                else:
                    small += 1

        return count