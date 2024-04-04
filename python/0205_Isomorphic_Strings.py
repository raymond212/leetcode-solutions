class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return
        ds = {}
        dt = {}
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = i
            if t[i] not in dt:
                dt[t[i]] = i
        for i in range(len(s)):
            if ds[s[i]] != dt[t[i]]:
                return False
        return True