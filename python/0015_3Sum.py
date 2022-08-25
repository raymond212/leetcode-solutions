class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  # Solution using 3 pointers. O(n^2) time, O(1) space
        if nums is None or len(nums) < 3:
            return []

        nums.sort()
        res = []
        first = 0

        while first < len(nums) - 2:
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1
                continue

            target = 0 - nums[first]
            left = first + 1
            right = len(nums) - 1

            while left < right:
                if left > first + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                tmp = nums[left] + nums[right]

                if tmp > target:
                    right -= 1
                elif tmp < target:
                    left += 1
                else:
                    res.append([nums[first], nums[left], nums[right]])
                    right -= 1
                    left += 1

            first += 1

        return res
