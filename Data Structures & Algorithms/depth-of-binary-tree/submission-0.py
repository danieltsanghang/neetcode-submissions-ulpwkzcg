# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return recur(root, 0)
        
def recur(n, depth):
    if not n:
        return depth
    return max(recur(n.left, depth+1), recur(n.right, depth+1))