class Solution:
    def findCrossingTime(self, n: int, k: int, time) -> int:
        def add(bank, i):
            heappush(bank, (-time[i][0] - time[i][2], -i))

        left_bank, right_bank = [], []
        for i in range(k):
            add(left_bank, i)

        t = assigned = received = 0
        events = []
        occupied = False

        while True:
            if not occupied:
                if right_bank:
                    worker = -heappop(right_bank)[1]
                    heappush(events, (t + time[worker][2], "r_to_l", worker))
                    occupied = True
                elif left_bank and assigned < n:
                    assigned += 1
                    worker = -heappop(left_bank)[1]
                    heapq.heappush(events, (t + time[worker][0], "l_to_r", worker))
                    occupied = True
            while events:
                t, job, worker = heapq.heappop(events)
                if job == "load":
                    add(right_bank, worker)
                elif job == "unload":
                    add(left_bank, worker)
                elif job == "l_to_r":
                    heappush(events, (t + time[worker][1], "load", worker))
                    occupied = False
                elif job == "r_to_l":
                    received += 1
                    if received == n:
                        return t
                    heappush(events, (t + time[worker][3], "unload", worker))
                    occupied = False
                if events and events[0][0] != t:
                    break
        return -1