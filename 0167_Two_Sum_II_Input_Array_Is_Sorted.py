class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None or len(numbers) < 2:
            return [-1, -1]

        left = 0
        right = len(numbers) - 1

        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]