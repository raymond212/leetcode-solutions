class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        mapping = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        res = ""
        for i in range(n + 1):
            after = self.direct_d(pattern, i)
            res += mapping[after]
            mapping.pop(after)
        return res

    def direct_d(self, pattern, index):
        count = 0
        for i in range(index, len(pattern)):
            if pattern[i] == "D":
                count += 1
            else:
                break
        return count