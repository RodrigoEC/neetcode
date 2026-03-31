class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        # What we need to do? Starting from a node we need the smallest amount
        # of time to get from the starting node to all its neighbors. The graph
        # will not always be connected so it may be impossible.

        # how should we do it? We'll need to run over all elements in the graph
        # because we don't know if that path takes more or less time then the
        # one we already coverd

        # What structure or algorithm should we use here? We'll use a DFS

        # What's the time complixity of this approach? O(V + E) number of
        # vertices + numer of edges



        neigh = { i: [].copy() for i in range(1, n + 1) }

        for [init, end, time] in times:
            neigh[init].append([end, time])
        
        print(neigh)

        res = [float('inf')] * (n + 1)

        def dfs(node, cost, visited):
            
            if node in visited:
                return
            
            res[node] = min(res[node], cost)

            visited.add(node)
            for [destiny, time] in neigh[node]:
                dfs(destiny, cost + time, visited)

            visited.remove(node)



        dfs(k, 0, set())
        return max(res[1:]) if float('inf') not in res[1:] else -1