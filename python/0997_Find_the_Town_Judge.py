class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        p = [0] * (n + 1) # p[i] = ppl who trust i - ppl who i trust

        for a, b in trust:
            p[a] -= 1
            p[b] += 1
        
        for i in range(1, n + 1):
            if p[i] == n - 1:
                return i

        return -1