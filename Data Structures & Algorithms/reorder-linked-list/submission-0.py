# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    #   split the list into 2, and combine the left half with the right half in reverse
        recur(head, head.next)
        # 012345[6] > 0612345 -> 1
        # 061234[5] > 0615234 -> 2
        # 061523[4] > 0615243 -> 3

def recur(root, current)-> Optional[ListNode]:
    if current is None:
        return root
    root = recur(root, current.next)
    if root is None:
        return None
    if root == current or root.next == current:
        current.next = None
        return None
    tmp = root.next
    root.next = current
    current.next = tmp
    print(root.val, current.val, tmp.val)
    return tmp
