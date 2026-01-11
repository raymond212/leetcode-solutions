class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        res = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '0':
                    heights[c] = 0
                else:
                    heights[c] += 1
            stack = []
            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    top = stack.pop()
                    height = heights[top]
                    left = stack[-1] + 1 if stack else 0
                    right = i - 1
                    width = right - left + 1
                    res = max(res, height * width)
                stack.append(i)
        return res
