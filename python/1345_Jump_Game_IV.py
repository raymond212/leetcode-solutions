class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mapping = {} # maps values to indices
        n = len(arr)
        for i in range(n):
            if arr[i] in mapping:
                mapping[arr[i]].append(i)
            else:
                mapping[arr[i]] = [i]
        
        visited = [False] * n
        visited[0] = True
        queue = collections.deque([0])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()
                if index == n - 1:
                    return steps
                
                right = index + 1
                left = index - 1
                
                if right < n and not visited[right]:
                    queue.append(right)
                    visited[right] = True
                if left >= 0 and not visited[left]:
                    queue.append(left)
                    visited[left] = True
                
                if arr[index] in mapping:
                    for next_index in mapping[arr[index]]:
                        if next_index == index or visited[next_index]:
                            continue

                        queue.append(next_index)
                        visited[next_index] = True
                    del mapping[arr[index]]
                
            steps += 1
            
        return -1