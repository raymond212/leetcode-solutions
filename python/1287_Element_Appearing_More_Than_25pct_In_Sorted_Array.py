class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        target = n / 4

        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate
            
        return -1