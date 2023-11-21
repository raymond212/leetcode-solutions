class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l, r, comb):
            if len(comb) == 2 * n:
                res.append(comb)
            if l < n:
                dfs(l + 1, r, comb + "(")
            if r < l:
                dfs(l, r + 1, comb + ")")

        res = []
        dfs(0, 0, "")   
        return res