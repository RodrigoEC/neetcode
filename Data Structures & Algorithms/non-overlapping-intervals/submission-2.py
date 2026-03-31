class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        # 1 2 3 4
        # _ _
        # _ _ _ _
        #   _ _ _


        # [[1,5], [2,3], [4,5]]

        # [[3, 1, 2], [5, 1, 4], [5, 4, 1]]

        # 0 0

        # What we need to do?  We need to get a way of finding the interval
        # that covers the biggest area and if it overlaps other interval we
        # should remove it, because if they start from the same point and
        # overlap we MUST remove one of them, so it's even better for us
        # that, if we want to optmize this and remove the fewest intervals, 
        # then we need to remove the biggest one

        # How should we do it? We'd sort the intervals array having the
        # interval's end and size as sorting keys. Once we do that we
        # will a variable that's the current start and everytime an end is
        # smaller than the current start we are going "pop it" and add one
        # to the count and move. When that doesn't happen we'll only have
        # to update the start variable

        # What structure/algorithm should I use? Sorting alrigthm and just
        # intervals logic

        # What's the time complexity of this solution? O(nlogn) 'cause of the
        # sorting


        # curEnd = 4
        # pops = 1

        # [[3, 1, 2], [5, 1, 4], [5, 4, 1]]



        intersArray = [[end, abs(end - start), start] for [start, end] in intervals]

        intersArray.sort()

        print(intersArray)

        curEnd = float('-inf')
        pops = 0
        for [end, size, start] in intersArray:

            if start >= curEnd:
                curEnd = end
            else:

                pops += 1

        
        return pops





























