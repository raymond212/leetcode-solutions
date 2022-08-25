class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        res = [1] * (n + 1)
        up = n
        down = 1
        for i in range(1, n):
            res[i] = res[i - 1] * up // down;
            up -= 1
            down += 1
        return res;