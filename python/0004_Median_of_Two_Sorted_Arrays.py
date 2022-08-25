class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n = len(a) + len(b)
        if n % 2 == 1:
            return self.find_kth(a, 0, b, 0, n // 2 + 1)
        else:
            return (self.find_kth(a, 0, b, 0, n // 2) + self.find_kth(a, 0, b, 0, n // 2 + 1)) / 2.0
    
    def find_kth(self, a, a_start, b, b_start, k):
        if a_start >= len(a):
            return b[b_start + k - 1]
        if b_start >= len(b):
            return a[a_start + k - 1]
        if k == 1:
            return min(a[a_start], b[b_start])
        a_index = a_start + k // 2 - 1 
        b_index = b_start + k // 2 - 1
        a_key = a[a_index] if a_index < len(a) else float('inf')
        b_key = b[b_index] if b_index < len(b) else float('inf')
        if a_key < b_key:
            return self.find_kth(a, a_start + k // 2, b, b_start, k - k // 2)
        else:
            return self.find_kth(b, b_start + k // 2, a, a_start, k - k // 2)