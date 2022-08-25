class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}
        
        for i in range(len(s)):
            bracket = s[i]
            if bracket in mapping: # open bracket
                stack.append(bracket)
            else: # closed bracket
                if len(stack) > 0 and mapping[stack[-1]] == bracket:
                    stack.pop()
                    continue
                return False

        return len(stack) == 0 