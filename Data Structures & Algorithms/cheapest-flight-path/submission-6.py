from collections import deque 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        


        # 1. Create a neighbors object se we can represent the graphs
        # node's relationships.
        #
        # 2. Implement a BFS with a limitation where the amount
        # of levels we're going to travel in the BFS equals to the k number
        # that's given
        # 
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrice = prices.copy()

            for s, d, p in flights:

                if prices[s] == float("inf"):
                    continue

                tmpPrice[d] = min(tmpPrice[d], prices[s] + p)
            
            prices = tmpPrice

        return -1 if prices[dst] == float("inf") else prices[dst]

