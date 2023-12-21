class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = [x for x, _ in points]
        arr.sort()

        ans = 0
        for i in range(1, len(arr)):
            ans = max(ans, arr[i] - arr[i - 1])
        
        return ans

