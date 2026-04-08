# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        acc = []
        self.recur(root, acc)
        print(acc) # this should be in order
        return acc[k-1]
    def recur(self, node, acc):
        if node is None:
            return
        self.recur(node.left, acc) # left is smaller
        acc.append(node.val) # then add self
        self.recur(node.right, acc) # then add bigger nodes
        return
