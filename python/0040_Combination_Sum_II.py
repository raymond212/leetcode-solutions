class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return [[]]
        candidates.sort()
        combinations = []
        self.dfs(candidates, 0, 0, target, [False] * len(candidates), [], combinations)
        return combinations
    
    def dfs(self, candidates, index, sum, target, visited, combination, combinations):
        if sum == target:
            combinations.append(list(combination))
            return
        
        for i in range(index, len(candidates)):
            if candidates[i] + sum > target or (i > 0 and candidates[i] == candidates[i - 1] and visited[i - 1] == False):
                continue
            combination.append(candidates[i])
            visited[i] = True
            self.dfs(candidates, i + 1, sum + candidates[i], target, visited, combination, combinations)
            visited[i] = False
            combination.pop()
            