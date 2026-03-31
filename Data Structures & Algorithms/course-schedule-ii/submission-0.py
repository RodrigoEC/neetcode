class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         

        # What we need to do? If there's a loop inside in this graph, it means that
        # the solution is impossible, therefore we should return []. But if there's
        # a valid solution then we could just run through the dependencies graph
        # and add to the solution's array in reverse order that we're accessing
        # this nodes

        # How should we do it? We could run a DFS on each course, if the course
        # was not yet visited then we run the DFS where we'll go through its 
        # dependencies (prerequisites) until we find - or not - the course that
        # we depend on and that doesn't depends on any other course. If we find that
        # we got in a loop then we need to return an empty array. 

        # What algorithms/structures should I use? The algorithm DFS, a set and 
        # probably arrays

        # What's the time complexity of this problem? I think this will by O(n), 
        # but let's see



        # numCourses = 3
        # prerequisites = [[1,0]]

        # res = []
        # visited = [0, 1, 2]
        # seen = []
        # nodes = [[],[0],[]]
        # 


        nodes = [[].copy() for _ in range(numCourses)]

        for [course, prereq] in prerequisites:
            nodes[course].append(prereq)

        visited = set()
        res = []        

        def dfs(node, seen):
            
            if node in seen:
                return False
            
            if node in visited:
                return True


            seen.add(node)

            for child in nodes[node]:

                if not dfs(child, seen):
                    return False

            seen.remove(node)
            res.append(node)
            visited.add(node)

            return True

        for node in range(numCourses):

            if node not in visited:
                
                if not dfs(node, set()):
                    return []
        
        return res




