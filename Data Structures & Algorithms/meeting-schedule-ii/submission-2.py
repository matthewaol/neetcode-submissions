"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0 

        if len(intervals) == 1: 
            return 1

        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()

        s = 0 
        e = 0
        count = 0 
        res = 0 
        while s < len(starts): 
            if starts[s] < ends[e]:
                count += 1
                s += 1
            elif starts[s] >= ends[e]:
                count -= 1 
                e += 1
            res = max(count, res)
        return res

