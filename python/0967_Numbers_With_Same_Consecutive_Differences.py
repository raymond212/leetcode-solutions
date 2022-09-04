class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        self.dfs(0, n, k, [], res)
        return res
    
    def dfs(self, index, n, k, num, res):
        if index == n:
            res.append(int(''.join([str(x) for x in num])))
            return
        if index == 0:
            for digit in range(1, 10):
                num.append(digit)
                self.dfs(1, n, k, num, res)
                num.pop()
        else:
            prev = num[index - 1]
            if prev + k <= 9:
                num.append(prev + k)
                self.dfs(index + 1, n, k, num, res)
                num.pop()
            if k != 0 and prev - k >= 0:
                num.append(prev - k)
                self.dfs(index + 1, n, k, num, res)
                num.pop()
        