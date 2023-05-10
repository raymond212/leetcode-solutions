class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        d = 1
        ans = []

        while bottom >= top and right >= left:
            if d == 1:
                for c in range(left, right + 1):
                    ans.append(matrix[top][c])
                top += 1
            elif d == 2:
                for r in range(top, bottom + 1):
                    ans.append(matrix[r][right])
                right -= 1
            elif d == 3:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1
            else:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1
            d = (d + 1) % 4
        
        return ans