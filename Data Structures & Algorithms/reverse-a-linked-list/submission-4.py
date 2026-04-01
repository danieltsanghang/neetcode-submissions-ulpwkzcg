# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = head # hold pointer to new head
        if head.next:
            newHead = self.reverseList(head.next) # replace node by next until end of listed list
            head.next.next = head # reverse direction
        head.next = None # remove old link
        return newHead
