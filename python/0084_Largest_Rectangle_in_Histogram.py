class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
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