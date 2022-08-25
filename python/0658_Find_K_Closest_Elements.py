class Solution:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return self.find_closest(nums, mid, mid, target, k)
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        return self.find_closest(nums, start, end, target, k)


    def find_closest(self, nums, left, right, target, k):
        count = 0
        res = []
        while count < k:
            if left >= 0 and right < len(nums):
                if left == right:
                    right += 1
                    left -= 1
                elif nums[right] - target < target - nums[left]:
                    right += 1
                else:
                    left -= 1
                count += 1
                continue
            if left >= 0:
                left -= 1
            if right < len(nums):
                right += 1
            count += 1
        
        for i in range(left + 1, right):
            res.append(nums[i])
            
        return res        