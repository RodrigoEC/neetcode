class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        diffs = { target - num: i for i, num in enumerate(nums) }


        for i, num in enumerate(nums):
            if num in diffs and diffs[num] != i:
                return [i, diffs[num]]

            