class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        dx = c[1][0] - c[0][0]
        dy = c[1][1] - c[0][1]
        for i in range(2, len(c)):
            cdx = c[i][0] - c[0][0]
            cdy = c[i][1] - c[0][1]
            if cdx * dy != cdy * dx:
                return False
        return True