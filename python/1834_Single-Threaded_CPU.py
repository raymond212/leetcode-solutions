from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for idx in range(n):
            tasks[idx].append(idx)
        tasks.sort()

        time = 1
        task = 0
        ans = []
        available = []

        while task < len(tasks) or available:
            if not available and tasks[task][0] > time:
                time = tasks[task][0]
            while task < len(tasks) and tasks[task][0] <= time:
                heappush(available, (tasks[task][1], tasks[task][2]))
                task += 1
            process_time, label = heappop(available)
            ans.append(label)
            time += process_time
        
        return ans