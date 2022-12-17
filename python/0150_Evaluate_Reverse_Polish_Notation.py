class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))
        return stack.pop()