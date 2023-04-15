class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while pushed and popped:
            if stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            else:
                stack.append(pushed[0])
                pushed.pop(0)
        return stack == popped[::-1]
