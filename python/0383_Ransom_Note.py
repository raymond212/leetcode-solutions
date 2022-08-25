class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rFreq = self.getFreq(ransomNote)
        mFreq = self.getFreq(magazine)
        for i in range(26):
            if rFreq[i] > mFreq[i]:
                return False
        return True
        
    def getFreq(self, s):
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
        return freq