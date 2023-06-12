class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []
        i = 0

        while i < n:
            cur = nums[i]
            while i + 1 < n and nums[i + 1] - nums[i] == 1:
                i += 1
                
            if nums[i] == cur:
                ans.append(str(cur))
            else:
                ans.append("{}->{}".format(cur, nums[i]))
            i += 1

        return ans