from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        mp = defaultdict(set)
        for a, b in dislikes:
            mp[a].add(b)
            mp[b].add(a)
        
        q = deque([(1, 0)])
        groups = [{1}, set()]
        remains = {i for i in range(2, n + 1)}

        while q:
            i, a = q.popleft()
            b = (a + 1) % 2
            for j in groups[a]:
                if j in mp[i]:
                    return False
            for dislike in mp[i]:
                if dislike in groups[b]:
                    continue
                groups[b].add(dislike)
                q.append((dislike, b))
                if dislike in remains:
                    remains.remove(dislike)
            if len(q) == 0:
                if len(remains) == 0:
                    return True
                q.append((remains.pop(), a))
        
        return False
                
