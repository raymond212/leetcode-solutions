class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return [[]]

        candidates = list(set(candidates))
        candidates.sort()
        combinations = []
        self.dfs(0, target, candidates, [], combinations)
        return combinations
    
    def dfs(self, index, target, candidates, combination, combinations):
        if target < 0:
            return

        if target == 0:
            combinations.append(list(combination))
            return
        
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            
            combination.append(candidates[i])
            self.dfs(i, target - candidates[i], candidates, combination, combinations)
            combination.pop()