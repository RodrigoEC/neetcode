class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        # What we need to do? We receibe a list of numbers that represent
        # a range between 0 and n but there's a number missing. We need to 
        # findout what number is this

        # How should we do it? We could sum all numbers in this current
        # range of values and subtract them from this sum. If we get a number
        # we return it but if we get 0 it can mean 2 things, either we are
        # missing the number 0 or we're missing the number max(nums) + 1

        # What structure or algorithm are we using? No structure, we're just going
        # to iterate through the array

        # What's the time complexity of this? This is going to be O(n) in time
        # and constant in space


        maxVal = max(nums)
        total = 0
        for i in range(maxVal + 1):
            total += i

        print(total)
        
        for num in nums:
            total -= num
    

        if total != 0:
            return total
        else:

            return 0 if 0 not in nums else maxVal + 1


