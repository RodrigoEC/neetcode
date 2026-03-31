class Node:

    def __init__(self, course, prerequisites=[]):

        self.course = course
        self.prerequisites = prerequisites.copy()


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        # What we need to do? Basically we need to check if we have a graph
        # with loops in it. If we do it means that at some point we will be
        # faced with a course that depends on itself to be taken by a student
        # which cannot happen


        # How should we do it? We could use a DFS approach combined with a visited
        # set. If we dive into this DFS and we get to a node that's already on the
        # visited set, then we find ourselves with a loop on this relation graph 


        # What structure should I use? This is a graph problem! So I could create
        # a class Node that has the course and it's prerequisites. I this would
        # make things more clear, even though it might take more time in terms of
        # lines of code it might take less time on debbuging

        # What's the complexity of this approach?


        nodes = { i: Node(i) for i in range(numCourses) }

        
        for i, node in nodes.items():
            print(i, node.prerequisites)
        for [clas, prer] in prerequisites:
            print('hey')
            nodes[clas].prerequisites.append(nodes[prer])

        for i, node in nodes.items():
            print(i, node.prerequisites)


        def dfs(node, visited):

            if not node:
                return True
        
            if node.course in visited:
                return False


            hasLoop = True

            visited.add(node.course)

            for prer in node.prerequisites:


                hasLoop = hasLoop and dfs(prer, visited)
            
            visited.remove(node.course)
            return hasLoop


        for i in range(numCourses):

            if not dfs(nodes[i], set()): return False
        
        return True








