# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 : [9,0,9]
        # l2 : [9,9,9]
        # re :N,8,1]

        # l1 : [9,0,9]
        # l2 : [9,9,9]
        # re : [8,0,1]

        # l1 : [9,0,9]
        # l2 : [9,9,9]
        # re : [8,0,9,1]
        head = ListNode()
        cur = head
        while l1 or l2:
            l1Val = 0 if l1 is None else l1.val
            l2Val = 0 if l2 is None else l2.val
            result = l1Val + l2Val + cur.val
            if cur.next:
                result += (cur.next.val * 10)
            
            remainder = result % 10
            # print("val for", l1Val, l2Val, 'is:', result, remainder)
            cur.val = remainder
            if result >= 10:
                cur.next = ListNode((result-remainder)//10)

            l1 = l1 if l1 is None else l1.next
            l2 = l2 if l2 is None else l2.next
            if (l1 or l2) and not cur.next:
                cur.next = ListNode()
            cur = cur.next
        return head
            
        