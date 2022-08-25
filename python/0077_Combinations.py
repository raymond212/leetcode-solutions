class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.dfs(0, n, k, [], combinations)
        return combinations
    
    def dfs(self, cur, n, k, combination, combinations):
        if k == 0:
            combinations.append(list(combination))
            return
        
        for i in range(cur, n - k + 1):
            combination.append(i + 1)
            self.dfs(i + 1, n, k - 1, combination, combinations)
            combination.pop()