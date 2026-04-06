class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        for pointer, point_num in enumerate(nums):
            if point_num > 0:
                break

            if pointer > 0 and point_num == nums[pointer - 1]:
                continue

            start = pointer + 1
            end = len(nums) - 1
            while start < end:
                # start_num = nums[start]
                # end_num = nums[end]
                # print(start_num, end_num)

                three_sum = point_num + nums[start] + nums[end]

                if three_sum > 0:
                    end -= 1
                elif three_sum < 0:
                    start += 1
                else:
                    res.append([point_num, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while  nums[start] == nums[start - 1] and start < end:
                        start += 1
                        

        return res
            

