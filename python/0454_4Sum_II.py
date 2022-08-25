class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dictionary = {}
        for a in A:
            for b in B:
                sum = a + b
                dictionary[a + b] = dictionary.get(sum, 0) + 1
        
        count = 0
        for c in C:
            for d in D:
                sum = c + d
                count += dictionary.get(-sum, 0)

        return count