class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i, candidate in enumerate(intervals):
            if candidate[1] < newInterval[0]: # target is after candidate
                continue
            elif candidate[0] > newInterval[1]: # target is before candidate
                intervals.insert(i, newInterval)
                return intervals
            intervals[i][0] = min(candidate[0], newInterval[0])
            intervals[i][1] = max(candidate[1], newInterval[1])
            while i + 1 < len(intervals) and intervals[i + 1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            return intervals
        intervals.append(newInterval)
        return intervals