class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1])) # earlier items will fit
        
        res = 0
        max_defense = 0
        
        for attack, defense in properties: 
            if defense < max_defense:
                res += 1
            else:
                max_defense = defense
        return res
            