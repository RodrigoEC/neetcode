import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        # min heap to store the intervals and then
        #
        # intervals = [[1,2],[1,4],[2,4]]
        # intervals = [[1,2],[1,4],[2,4]]
        
        # intervals = [[1,8],[2,3],[4,5]]
        # intervals = [[2,3],[4,5],[1,8]]
        #
        #
        #
        # removed = 1
        # cur_inter = [4,6]
        # intervals = [[4,6]]
        # 
        # 
        #
        intervals.sort(key=lambda x: x[1])

        removed = 0
        cur_inter = None
        print(intervals)

        for i, interval in enumerate(intervals):

            if not cur_inter:
                cur_inter = interval
                continue
            
            if interval[0] < cur_inter[1]:
                removed += 1
            else:
                cur_inter = interval
        
        return removed

        

