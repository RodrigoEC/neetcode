class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # 


        start, end = 0, len(heights) - 1

        max_area = 0
        while start < end:
            l_height = heights[start]
            r_height = heights[end]

            cur_area = min(l_height, r_height) * (end - start)

            max_area = max(cur_area, max_area)

            if l_height < r_height:
                start += 1
            else:
                end -= 1

        return max_area
