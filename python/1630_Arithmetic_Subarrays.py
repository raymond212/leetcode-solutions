class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(seq):
            l = len(seq)
            min_val = min(seq)
            rng = max(seq) - min_val

            if rng == 0:
                return True
            if rng % (l - 1) != 0:
                return False

            diff = rng // (l - 1)
            visited = [False] * l

            for num in seq:
                if (num - min_val) % diff != 0:
                    return False
                visited[(num - min_val) // diff] = True
            
            return False not in visited
        
        return [check(nums[start:end + 1]) for start, end in zip(l, r)]