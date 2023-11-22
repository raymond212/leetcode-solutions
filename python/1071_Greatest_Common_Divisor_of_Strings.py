class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)

        d = gcd(n1, n2)
        t = str1[:d]

        if str1 == t * (n1 // d) and str2 == t * (n2 // d):
            return t
        return ''
