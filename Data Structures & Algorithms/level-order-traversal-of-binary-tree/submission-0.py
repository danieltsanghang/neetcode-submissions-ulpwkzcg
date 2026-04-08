# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        recur(root, 0, res)
        print(list(res.values()))
        return list(res.values())

def recur(n, depth, mp):
    if not n:
        return
    mp[depth] += [n.val]
    recur(n.left, depth+1, mp)
    recur(n.right, depth+1, mp)
    return
