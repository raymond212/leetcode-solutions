class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapify(nums)
        
        ans = 0
        for _ in range(k):
            val = -heappop(nums)
            ans += val
            heappush(nums, -(math.ceil(val / 3)))
        return ans