class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all([x % 2 == 0 for x in Counter(nums).values()])