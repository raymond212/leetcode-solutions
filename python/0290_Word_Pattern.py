class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        dict = {}
        visited = set()

        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            if letter in dict and word != dict[letter]:
                return False
            if letter not in dict:
                if word in visited:
                    return False
                
                dict[letter] = word
                visited.add(word)

        return True 
