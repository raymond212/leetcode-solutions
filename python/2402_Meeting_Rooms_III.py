import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        freq = [0] * n
        endTimes = [] # heap of (endTime, room)
        occupied = 0
        rooms = [False] * n
        
        for start, end in meetings:
            while len(endTimes) > 0 and endTimes[0][0] <= start:
                endTime, room = heapq.heappop(endTimes)
                occupied -= 1
                rooms[room] = False
            if occupied < n: # if there is space
                room = self.firstEmpty(rooms)
                freq[room] += 1
                occupied += 1
                rooms[room] = True
                heapq.heappush(endTimes, (end, room))
            else:                
                prevEnd, room = heapq.heappop(endTimes)
                newEnd = prevEnd - start + end
                freq[room] += 1
                heapq.heappush(endTimes, (newEnd, room))
                
        mostFreq = max(freq)
        for i in range(n):
            if freq[i] == mostFreq:
                return i
                
    def firstEmpty(self, rooms):
        for i in range(len(rooms)):
            if rooms[i] == False:
                return i
        return len(rooms)