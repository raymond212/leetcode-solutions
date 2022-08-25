class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in mapping:
                mapping[key].append(s)
            else:
                mapping[key] = [s]
        return mapping.values()