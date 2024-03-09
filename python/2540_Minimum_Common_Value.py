class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            x, y = nums1[i], nums2[j]
            if x == y:
                return x
            elif x < y:
                i += 1
            else:
                j += 1
        return -1
            