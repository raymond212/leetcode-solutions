class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)
        res = [False] * n

        for i, num in enumerate(candies):
            res[i] = num + extraCandies >= max_candies
        
        return res