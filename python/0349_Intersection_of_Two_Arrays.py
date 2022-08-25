# Two pointers: Time O(m log m + n log n), Space: O(1)
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = set()
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
        return list(intersection)
        
    
# Hashset: Time O(m + n), Space: O(max(n, m))
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))

# Alternative: sort nums2, and then binary search if each element in nums1 is in nums2. Time O(m log m + n log m), Space: O(1)