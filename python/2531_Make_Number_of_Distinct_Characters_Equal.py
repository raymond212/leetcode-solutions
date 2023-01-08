class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in range(len(word1)):
            freq1[ord(word1[i]) - ord('a')] += 1
        for i in range(len(word2)):
            freq2[ord(word2[i]) - ord('a')] += 1
        
        for i in range(26):
            for j in range(26):
                if freq1[i] == 0 or freq2[j] == 0:
                    continue
                freq1[i] -= 1
                freq2[j] -= 1
                freq1[j] += 1
                freq2[i] += 1
                if self.countNonZero(freq1) == self.countNonZero(freq2):
                    return True
                freq1[i] += 1
                freq2[j] += 1
                freq1[j] -= 1
                freq2[i] -= 1
        return False
    
    def countNonZero(self, a):
        count = 0
        for i in range(len(a)):
            if a[i] != 0:
                count += 1
        return count