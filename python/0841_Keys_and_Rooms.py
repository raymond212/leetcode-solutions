import collections

class Solution:
    def canVisitAllRooms(self, keys: List[List[int]]) -> bool:
        visited = {0}
        q = collections.deque([0])
        while q:
            room = q.popleft()
            for next_room in keys[room]:
                if next_room in visited:
                    continue
                q.append(next_room)
                visited.add(next_room)
        return len(visited) == len(keys)