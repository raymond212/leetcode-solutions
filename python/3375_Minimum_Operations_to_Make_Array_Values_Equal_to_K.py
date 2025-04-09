class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = set(nums)
        if min(a) < k:
            return -1
        return len(a) - (1 if min(a) == k else 0)