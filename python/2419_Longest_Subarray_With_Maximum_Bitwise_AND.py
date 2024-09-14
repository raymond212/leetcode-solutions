class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        streak = 0
        ans = 0

        for num in nums:
            if num > max_val:
                max_val = num
                ans = streak = 0
            if num == max_val:
                streak += 1
            else:
                streak = 0
            ans = max(ans, streak)

        return ans