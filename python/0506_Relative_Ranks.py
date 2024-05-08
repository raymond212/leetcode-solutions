class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = sorted(score, reverse=True)
        rank = {arr[i]: i for i in range(len(score))}
        mp = ['Gold', 'Silver', 'Bronze']
        return [str(rank[x] + 1) if rank[x] > 2 else f'{mp[rank[x]]} Medal' for x in score]