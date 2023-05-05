class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        num_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                num_vowels += 1
        
        ans = num_vowels

        for i in range(k, len(s)):
            if s[i] in vowels:
                num_vowels += 1
            if s[i - k] in vowels:
                num_vowels -= 1
            ans = max(num_vowels, ans)
        
        return ans
