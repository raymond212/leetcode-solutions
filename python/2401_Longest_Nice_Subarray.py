# Solution during contest
class Solution1:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        binary_nums = [str(bin(nums[i]))[2:] for i in range(n)]
        len_max = len(str(bin(max(nums)))) - 2
        longest_from = [1] * n
        for i in range(n):
            tally = [0] * len_max
            bad = False
            doneJ = n
            for j in range(i, n):
                binary_j = binary_nums[j]
                for k in range(len(binary_j)):
                    if binary_j[len(binary_j) - k - 1] == "1":
                        if tally[k] == 1: # bad
                            doneJ = j
                            bad = True
                            break
                        else:
                            tally[k] = 1
                if bad:
                    break
            longest_from[i] = doneJ - i
        return max(longest_from)

# Using sliding window
class Solution2:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = AND = i = 0
        for j in range(len(nums)):
            while AND & nums[j]:
                AND ^= nums[i]
                i += 1
            AND |= nums[j]
            res = max(res, j - i + 1)
        return res