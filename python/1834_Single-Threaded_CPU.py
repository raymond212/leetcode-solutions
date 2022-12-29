from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for idx in range(n):
            tasks[idx].append(idx)
        tasks.sort()

        time = 1
        ans = []
        available = []

        while tasks or available:
            if not available and tasks[0][0] > time:
                time = tasks[0][0]
            while tasks and tasks[0][0] <= time:
                heappush(available, (tasks[0][1], tasks[0][2]))
                tasks.pop(0)
            process_time, label = heappop(available)
            ans.append(label)
            time += process_time
        
        return ans