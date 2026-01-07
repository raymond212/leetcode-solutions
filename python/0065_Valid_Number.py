class Solution:
    def isNumber(self, s: str) -> bool:        
        stack = list(s[::-1])
        if stack and stack[-1] in '+-':
            stack.pop()

        has_number = False
        has_decimal = False
        while stack:
            if stack[-1].isdigit():
                stack.pop()
                has_number = True
            elif stack[-1] == '.' and not has_decimal:
                stack.pop()
                has_decimal = True
            else:
                break
        
        if not has_number:
            return False
        
        if has_number and stack and stack[-1] in 'eE':
            stack.pop()

            has_number = False
            if stack and stack[-1] in '+-':
                stack.pop()
            while stack and stack[-1].isdigit():
                stack.pop()
                has_number = True
            if not has_number:
                return False
        
        return len(stack) == 0