class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bitsPos1 = self.bitsPos(num1)
        bitsNum1 = len(bitsPos1)
        bitsNum2 = len(self.bitsPos(num2))
        
        res = []
        
        for i in range(min(bitsNum1, bitsNum2)):
            res.append(bitsPos1[bitsNum1 - 1 - i])
            bitsNum2 -= 1
        
        if bitsNum2 > 0:
            for i in range(32):
                if bitsNum2 == 0:
                    break
                if i in bitsPos1:
                    continue
                else:
                    res.append(i)
                    bitsNum2 -= 1
        
        res.sort()
        ans = 0
        
        for i in range(31, -1, -1):
            ans *= 2
            if i in res:
                ans += 1
        
        return ans
            
    def bitsPos(self, num):
        res = []
        for i in range(32):
            if num & 1:
                res.append(i)
            num = num >> 1
        return res