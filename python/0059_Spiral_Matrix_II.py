class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        ans = [[0] * n for _ in range(n)]
        cnt = 1
        d = 1

        while bottom >= top and right >= left:
            if d == 1:
                for c in range(left, right + 1):
                    ans[top][c] = cnt
                    cnt += 1
                top += 1
            elif d == 2:
                for r in range(top, bottom + 1):
                    ans[r][right] = cnt
                    cnt += 1
                right -= 1
            elif d == 3:
                for c in range(right, left - 1, -1):
                    ans[bottom][c] = cnt
                    cnt += 1
                bottom -= 1
            else:
                for r in range(bottom, top - 1, -1):
                    ans[r][left] = cnt
                    cnt += 1
                left += 1
            d = (d + 1) % 4
        
        return ans