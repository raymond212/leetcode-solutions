class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        visited[start] = True
        
        queue = collections.deque([start])
        
        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            right = index + arr[index]
            left = index - arr[index]
            if right < n and not visited[right]:
                queue.append(right)
                visited[right] = True
            if left >= 0 and not visited[left]:
                queue.append(left)
                visited[left] = True
        
        return False