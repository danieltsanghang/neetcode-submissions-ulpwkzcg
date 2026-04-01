# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # tmp = list1 if list1.val <= list2.val and (list1.next is None or list1.next.val >= list2.val) else list2
        # head = list1 if list1.val <= list2.val else list2

        # head.next = mergeTwoLists(list1)
        # return head
        # head = list1 if list1.val <= list2.val else list2
        # while list1 and list2:
        #     print(list1, list2)
        #     if list1.val <= list2.val:
        #         if list1.next is None or list1.next.val >= list2.val:
        #             list2End = list2.next
        #             list2.next = list1.next
        #             list1.next = list2
        #             list1, list2 = list2.next, list2End
        #         else:
        #             list1, list2 = list1.next, list2
        #     else:
        #         if list2.next is None or list2.next.val >= list1.val:
        #             list1End = list1.next
        #             list1.next = list2.next
        #             list2.next = list1
        #             list1, list2 = list1End, list2.next
        #         else:
        #             list1, list2 = list1, list2.next
        # return head


        # [1-1]-2-4
        # 3-5

        # 

