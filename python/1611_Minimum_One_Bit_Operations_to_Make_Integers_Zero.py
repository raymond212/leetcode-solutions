class Solution1:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans

class Solution2:
    def minimumOneBitOperations(self, n: int) -> int:
        bits = bin(n)[2:][::-1]

        def dfs(i, target):
            if i == 0:
                return 1 if bits[0] != target[0] else 0
            l = len(target)
            if bits[i] == target[i]:
                return dfs(i - 1, target[:l - 1])
            else:
                return dfs(i - 1, '0' * (l - 2) + '1') + 2 ** (l - 1)

        return dfs(len(bits) - 1, '0' * len(bits))

