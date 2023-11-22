class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        res = []

        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                mp[r + c].append(nums[r][c])
        
        diag = 0
        while diag in mp:
            res.extend(mp[diag])
            diag += 1
        
        return res