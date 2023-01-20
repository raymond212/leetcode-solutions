class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        seq = []

        def dfs(index):
            if index == len(nums):
                if len(seq) >= 2:
                    ans.add(tuple(seq))
                return
            if not seq or seq[-1] <= nums[index]:
                seq.append(nums[index])
                dfs(index + 1)
                seq.pop()
            dfs(index + 1)

        dfs(0)
        return ans