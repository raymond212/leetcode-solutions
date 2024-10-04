class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot = sum(skill) // (len(skill) // 2)
        freq = dict(Counter(skill))
        res = 0
        for s in freq:
            t = tot - s
            if t in freq and freq[s] == freq[t]:
                res += s * t * freq[s]
            else:
                return -1
        return res // 2