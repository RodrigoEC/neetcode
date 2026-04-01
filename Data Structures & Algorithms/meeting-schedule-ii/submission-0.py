"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # What we need to do?
        #
        # intervals = [(0,40),(5,10),(15,20)]
        #              0.                   40  
        #                 5  10 
        #                         15 20
        #
        # 

        # How should we do it?
        #
        # intervals = [(0, 12), (5, 10), (7, 20), (10, 12), (10, 20), (12, 20) (12, 15), (15, 20)]
        # 
        # rooms = 1
        # init = 15
        # end = 20
        #
        #       ------------
        #           ------      ---
        #               --------------
        #
        #
        #.
        # 1. The first element of the next tuple is bigger than
        # the current last element -> Reset rooms and move on <3
        # 
        # 2. The first element of the next tuple is smaller than
        # the current last element -> We have an intersection
        #   
        #   2.1. The last element of the next tuple is bigger than
        #       the current last element -> 
        #
        #   2.2. The last element of the next tuple is smaller than
        #       the current last element -> 
        #
        # 

        
        res = 0
        print(intervals)


        intervals.sort(key=lambda x: x.start)

        init, end = 0,0
        rooms = 1
        while intervals:

            interval = intervals.pop(0)

            if interval.start >= end:
                init = interval.start
                end = interval.end
                rooms = 1
            else:
                
                if interval.end != end:
                    intervals.append(Interval(min(interval.end, end), max(interval.end, end)))
                
                rooms += 1
                init = max(interval.start, init)
                end = min(interval.end, end)
                intervals.sort(key=lambda x: x.start)
            
            res = max(rooms, res)

        return res
        








