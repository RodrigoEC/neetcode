class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # What we need to do? We need to use a binary search approach but
        # costumized so we can use it with a sorted array. Dependind on how
        # the array was rotated and which are the elements distribtuion in
        # it we might need to do different things.
        #
        # one thins we need to keep an eye on is that now we want the smallest
        # element in this array

        # e.g 01:
        # 
        # [3,4,5,6,1,2]
        #  L     M   R
        #          LM R
        #          LR
        # [4,5,0,1,2,3]
        #  L     M   R
        #  L M   R
        #      L R

        # [1,2,3,4,5,6]
        #  L     M   R
        #  L M   R
        #  L R
        #  LR


        # How should we do it? What we gotta do here as a regular binary search
        # we're going to have left, middle and right pointers, but if middle
        # pointer points to a number that's bigger than the one on the right
        # pointer we update the left pointer to be middle + 1 and otherwise
        # we update the right to be equal to middle

        # Which algorithm / structure are we using? We're using a binary search

        # What's the time complexity of this solution? O(log n)


        left, right = 0, len(nums) - 1

        while (left < right):


            middle = (right + left) // 2

            if (nums[middle] > nums[right]):
                left = middle + 1
            else:
                right = middle
        
        return nums[left]











