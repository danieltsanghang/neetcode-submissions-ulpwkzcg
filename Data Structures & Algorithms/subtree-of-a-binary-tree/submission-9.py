# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: # both null means they're the same
            return True
        elif not root or not subRoot: # either null means they're different
            return False
        if isSameTree(root, subRoot): # if starting current node its the same tree return True
            return True
        # check sub tree 1 level down
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
def isSameTree(a, b):
    if not a and not b: # both null means they're the same
        return True
    elif not a or not b: # either null means they're different
        return False
    else: # check current val and continue to check sub nodes
        return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)