class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        slopes = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                slope = "inf" # vertical slope as default
                if x1 != x2:
                    slope = str((y2 - y1) / (x2 - x1))
                slopes[i][slope] += 1
                slopes[j][slope] += 1
            ans = max(ans, max(slopes[i].values())+ 1)
        return ans
