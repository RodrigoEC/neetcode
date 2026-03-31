class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # What we need to do? We need to find what are the sequences inside
        # inside this nums array.

        # setNums = set([[2,20,10,3,4,5]])

        # nums = [2,20,4,10,3,4,5]
        #           P

        # How should we do it? we're talking about finding sequences and its
        # lengths. For this problem we need to find the beginning of each
        # sequence. Once we have that information we can iterate adding one
        # unit to the current number until that result number is not on the list
        # animore, once we do it we're going to have that sequence's length.
        # We'll get the biggest sequece of the found sequences

        # What's the algorithm or structure needed? Just and array and a set

        # What's the time complexity of this approach? O(n)



        setNums = set(nums)

        biggestSub = 0
        for num in nums:

            if (num - 1 in setNums):
                continue
            
            curNum = num
            while curNum in setNums:
                curNum += 1

            biggestSub = max(biggestSub, curNum - num)
        
        return biggestSub
            

            