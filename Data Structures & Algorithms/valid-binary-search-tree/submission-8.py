# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min=None, max=None) -> bool:
        # flatten the tree and see if its sorted
        # [5,4,6,null,null,3,7] becomes [5] -> [5,6] -> [5,3,6] X
        #  at 3, we have a min/max window of (5--6)
        if root is None:
            return True
        if min is None and max is None:
            return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)
        tmp = self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)
        if min is None:
            return root.val < max and tmp
        elif max is None:
            return root.val > min and tmp
        else:
            return min < root.val < max and tmp

            


