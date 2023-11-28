class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seatCnt, plantCnt = 0, 0
        ans = 1
        for c in corridor:
            if seatCnt and seatCnt % 2 == 0:
                if c == 'S':
                    ans *= (plantCnt + 1)
                    plantCnt = 0
                else:
                    plantCnt += 1
            if c == 'S':
                seatCnt += 1

        return ans % (10 ** 9 + 7) if seatCnt and seatCnt % 2 == 0 else 0
            