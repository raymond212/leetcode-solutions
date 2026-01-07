class Solution:
    def addBinary(self, a: str, b: str) -> str:
        arr = []
        carry = 0
        m, n = len(a), len(b)
        a, b = a[::-1], b[::-1]
        for i in range(0, max(m, n)):
            bit1 = 0 if i >= m else int(a[i])
            bit2 = 0 if i >= n else int(b[i])
            cur = carry + bit1 + bit2
            arr.append(str(cur & 1))
            carry = cur >> 1
        if carry == 1:
            arr.append("1")
        return ''.join(arr[::-1])