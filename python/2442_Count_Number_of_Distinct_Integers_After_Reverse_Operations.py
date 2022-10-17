class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(int(str(x)[::-1]) for x in nums).union(set(nums)))  