class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # What we need to do? Since the only thing we can control on the
        # area of this container is the distance between the bars. We need 
        # to get the bigger area for each specific distance.
        # 

        # How should we do it? We could put two pointers - one on the start of
        # the list and the other one at the end - by doing that we first have the
        # biggest area for that specific distance - the biggest possible distance
        # - and we are going to update the distance - pointer - at the smallest
        # bar. If the smallest bar is on the right we shift the end pointer to
        # the left and it's on the left we shift it to the right and by doing
        # that we are going to have always the biggest area for each possible 
        # distance

        # What structure/algorithm we should use? two pointer

        # What's the complexity of this solution? O(n)


        # area = 36
        # [1,7,2,5,4,7,3,6]
        #      L                
        #            R

        start, end = 0, len(heights) - 1

        area = 0
        while start <= end:

            newArea = (end - start) * min(heights[start], heights[end])


            area = max(newArea, area)

            if (heights[start] >= heights[end]):
                end -= 1
            else:
                start += 1
        
        return area
