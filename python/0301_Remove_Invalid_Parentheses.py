class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        results = set()
        to_remove = self.count_invalid(s)
        self.dfs(0, s, [], to_remove, results)
        return list(results)
        
    def dfs(self, index, s, result, to_remove, results):
        if index == len(s):
            if to_remove > 0:
                return
            result_str = "".join(result)
            if self.count_invalid(result_str) == 0:
                results.add(result_str)
            return
        
        if to_remove > 0 and (s[index] == "(" or s[index] == ")"):
            self.dfs(index + 1, s, result, to_remove - 1, results) # removed
            
        result.append(s[index]) 
        self.dfs(index + 1, s, result, to_remove, results) # not removed
        result.pop()
    
    def count_invalid(self, s):
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            elif s[i] ==  ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right