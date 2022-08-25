MAPPING = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations
    
    def dfs(self, digits, index, combination, combinations):
        if index == len(digits):
            combinations.append(''.join(combination))
            return
        
        for letter in MAPPING[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index + 1, combination, combinations)
            combination.pop()
        