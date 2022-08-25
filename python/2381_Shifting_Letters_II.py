class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        n = len(s)
        d = [0] * (n+1)
        for l, r, t in shifts:
            if t:
                d[l] += 1
                d[r + 1] -= 1
            else:
                d[l] -= 1
                d[r + 1] += 1
        cur = 0
        t = []
        for i in range(n):
            cur += d[i]
            z = (ord(s[i]) - 97 + cur) % 26
            t.append(chr(z + 97))
        return "".join(t)