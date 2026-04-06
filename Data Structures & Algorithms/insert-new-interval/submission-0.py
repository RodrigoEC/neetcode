class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        # We're going to iterate through the intervals
        # and if the end value of the current element is
        # bigger than the init value of the new interval
        # we're merging these two by creating a new new interval
        # that's a merge version of those two and moving on to
        # the next interval.
        #
        # if the new init of the current interval is greater than the 
        # end of the new interval we just add the new interval to the 
        # res and also the rest of the intervals
        #
        # We could have a "merged" variable
        #
        #

        res = []
        merged = False
        for [init, end] in intervals:
            if merged:
                res.append([init, end])
                continue

            if init > newInterval[1]:
                merged = True
                res.append(newInterval)
                res.append([init, end])

            elif end >= newInterval[0]:
                print(newInterval, [init, end], newInterval)
                newInterval = [min(init, newInterval[0]), max(end, newInterval[1])]
            else:
                res.append([init, end])


        if not merged:
            res.append(newInterval)
        return res










