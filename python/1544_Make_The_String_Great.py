class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        diff = ord('a') - ord('A') 
        
        for i in range(len(s)):
            if stack and abs(ord(s[i]) - ord(stack[-1])) == diff:
                stack.pop()
            else:
                stack.append(s[i])
                
        return ''.join(stack)