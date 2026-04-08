"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        new_nodes = {}

        q = deque([node])


        while q:
            cur_node = q.popleft()

            if not new_nodes.get(cur_node):
                new_nodes[cur_node] = Node(cur_node.val)

                if cur_node.neighbors:
                    for nei in cur_node.neighbors:
                        q.append(nei)

        print(new_nodes)  


        for n in new_nodes.keys():

            if n.neighbors:
                for nei in n.neighbors:
                    if not new_nodes[n].neighbors:
                        new_nodes[n].neighbors = [new_nodes[nei]]
                    else:
                        new_nodes[n].neighbors.append(new_nodes[nei])

        return new_nodes.get(node)

            