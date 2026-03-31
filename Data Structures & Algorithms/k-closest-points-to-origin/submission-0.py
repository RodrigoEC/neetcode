class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        # What we need to do? We're given an array of points and we need
        # to calculate the distance of these points to the origin and then
        # return k closest points


        # How should we do it? We could calculate each distance and then use
        # a min heap to store the distances kind of sorted and, finally, we
        # pop from the heap k times and we'll have the k closest points

        # What structure or algorithm is more appropriate? We could use a heap

        # What's the time complexity of this approach? O(k * log n) because to
        # pop each value would log n time and we would do that k times


        # points = [[0,2],[2,0],[2,2]]
        # heap = [[4, [0,2]], [4, [2,0]], [8, [2,2]]]
        # 



        heap = [[x**2 + y**2, [x,y]] for [x, y] in points]

        heapq.heapify(heap) # O(n)

        res = []
        while k:

            [distance, coords] = heapq.heappop(heap)
            res.append(coords)

            k -= 1
        
        return res