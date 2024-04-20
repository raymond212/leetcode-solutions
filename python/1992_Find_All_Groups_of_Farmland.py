class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        
        def removeGroup(r, c):
            r1 = r2 = r
            c1 = c2 = c
            while r2 + 1 < m and land[r2 + 1][c] == 1:
                r2 += 1
            while c2 + 1 < n and land[r][c2 + 1] == 1:
                c2 += 1
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    land[r][c] = 0
            return [r1, c1, r2, c2]
        
        ans = []
        for r in range(m):
            for c in range(n):
                if land[r][c] == 1:
                    ans.append(removeGroup(r, c))
        return ans