# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        tmp = head
        while tmp is not None:
            size += 1
            tmp = tmp.next
        removeIndex = size - n
        if removeIndex == 0:
            return head.next
        tmp = head
        last = head
        while removeIndex != 1:
            last = last.next
            removeIndex -= 1
        last.next = last.next.next
        return head
            