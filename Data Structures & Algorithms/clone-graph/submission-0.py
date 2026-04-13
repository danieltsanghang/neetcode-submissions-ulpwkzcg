"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node'], visited=None) -> Optional['Node']:
        if node is None:
            return None
        visited = visited if visited is not None else {}
        newnode = Node(node.val)
        visited[node.val] = newnode
        neighbors = []
        for n in node.neighbors:
            if n is None:
                continue
            print(node.val, 'neighbors', n.val)
            if n.val in visited:
                neighbors.append(visited[n.val])
            else:
                neighbors.append(self.cloneGraph(n, visited))
        newnode.neighbors = neighbors
        visited[node.val] = newnode
        return newnode
        