class Solution:
    def countNegatives(self, grid) -> int:
        l = len(grid[0])
        j = l - 1
        ans = 0

        for i in range(len(grid)):
            while (j >= 0 and grid[i][j] < 0):
                j -= 1
            ans += (l - j - 1)
        
        return ans