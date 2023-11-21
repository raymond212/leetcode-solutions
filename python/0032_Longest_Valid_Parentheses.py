class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack represents the invalid indices
        stk = [-1]
        ans = 0

        for i in range(len(s)):
            if s[i] == ')' and len(stk) > 1 and s[stk[-1]] == '(':
                stk.pop()
                ans = max(ans, i - stk[-1])
            else:
                stk.append(i) 
        
        return ans