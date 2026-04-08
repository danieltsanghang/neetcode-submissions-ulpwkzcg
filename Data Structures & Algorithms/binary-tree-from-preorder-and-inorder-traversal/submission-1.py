# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            # print('preorder', preorder, 'inorder', inorder)
            return None
        rootVal = preorder[0]
        # print('preorder', preorder, 'inorder', inorder, 'cur', rootVal)

        pos = inorder.index(rootVal)
        left_inorder, right_inorder = inorder[:pos], inorder[pos+1:]
        left_preorder, right_preorder = preorder[1:pos+1], preorder[pos+1:]
        return TreeNode(rootVal, self.buildTree(left_preorder, left_inorder), self.buildTree(right_preorder, right_inorder))

