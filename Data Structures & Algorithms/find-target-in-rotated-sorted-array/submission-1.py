class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #
        #
        # sub_list = [3,5,6,0,1,2] target = 1
        #             L.    M.  R.
        #


        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)

            if target == nums[mid]:
                return mid
            
            if nums[left] > nums[mid]:
                if target > nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

