# two pointers contracting window
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        res = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        
        return res

# two pass solution. DP
class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        
        return res