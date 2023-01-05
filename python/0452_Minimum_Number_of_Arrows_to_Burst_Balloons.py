class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        # end of range to shoot arrow
        range_end = points[0][1] 
        for start, end in points:
            # if outside of the range that bursts current balloons, then start a new range
            if start > range_end: 
                ans += 1
                range_end = end
            # update range to also pop current balloon
            else:
                range_end = min(range_end, end)
        # add the last range
        ans += 1
        return ans