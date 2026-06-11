class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        middle = (r + l) // 2
        while l <= r:

            middle = (r + l) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        
        return middle if nums[middle] == target else -1