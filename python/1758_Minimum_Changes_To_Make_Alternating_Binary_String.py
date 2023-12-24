class Solution:
    def minOperations(self, s: str) -> int:
        startZero = startOne = 0

        for i in range(len(s)):
            startZeroCur = '0' if i % 2 == 0 else '1'
            if s[i] == startZeroCur:
                startOne += 1
            else:
                startZero += 1
                
        return min(startZero, startOne)