# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        cur = head
        while cur:
            if cur.val in visited and cur.next is not None:
                return True
            visited += [cur.val]
            cur = cur.next
        return False