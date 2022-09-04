class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        startPos, endPos = min(startPos, endPos), max(startPos, endPos)
        dif = endPos - startPos
        if dif > k or dif % 2 != k % 2:
            return 0
        netLeft = (k - dif) // 2 # Answer is k choose netLeft
        ans = 1
        for i in range(netLeft):
            ans *= (k - i)
        for i in range(1, netLeft + 1):
            ans //= i
        mod = int(1E9 + 7)
        return ans % mod
        