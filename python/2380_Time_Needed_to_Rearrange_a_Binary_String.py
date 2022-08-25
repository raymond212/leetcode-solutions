class Solution:
    def secondsToRemoveOccurrences(self, s_s: str) -> int:
        res = 0
        while '01' in s_s:
            s_s = s_s.replace('01', '10')
            res += 1
        return res
        # seconds = 0
        # s = list(s_s)
        # indices = set()
        # for i in range(len(s) - 1):
        #     if s[i] == "0" and s[i + 1] == "1":
        #         indices.add(i)
        # if len(indices) == 0:
        #     return 0
        # while True:
        #     seconds += 1
        #     new_set = set()
        #     for i in indices:
        #         s[i] = "1"
        #         s[i + 1] = "0"
        #     min_i = min(indices)
        #     for i in indices:
        #         if i + 2 < len(s) and s[i + 2] == "1":
        #             new_set.add(i + 1)
        #         if i > 0 and s[i - 1] == "0":
        #             new_set.add(i - 1)
        #     if len(new_set) == 0:
        #         break
        #     indices = new_set
        # return seconds