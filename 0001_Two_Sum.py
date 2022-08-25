class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in mp:
                return i, mp[remain]
            mp[nums[i]] = i

