class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = set()
        for word in words:
            codes.add(self.morse_code(word))
        return len(codes)
        
    def morse_code(self, word):
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = ""
        for c in word:
            code += mapping[ord(c) - ord('a')]
        return code