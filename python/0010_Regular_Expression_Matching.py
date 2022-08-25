class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, 0, p, 0, {})
    
    def dfs(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            if (j < len(p) and p[j] == "*") or (j < len(p) - 1 and p[j + 1] == "*"):
                memo[(i, j)] = self.dfs(s, i, p, j + 1, memo)
                return memo[(i, j)]
            return len(p) == j 
        
        if len(p) == j:
            return False   

        if p[j] != "*":
            if j < len(p) - 1 and p[j + 1] == "*":
                result = self.dfs(s, i, p, j + 1, memo)
            else:
                result = (s[i] == p[j] or p[j] == ".") and self.dfs(s, i + 1, p, j + 1, memo)
        else:
            if p[j - 1] == "." or s[i] == p[j - 1]:
                result = self.dfs(s, i + 1, p, j, memo) or self.dfs(s, i, p, j + 1, memo)
            else: # s[i] not equal to p[j - 1], only option is for * to be nothing
                result = self.dfs(s, i, p, j + 1, memo)
        
        memo[(i, j)] = result
        return result