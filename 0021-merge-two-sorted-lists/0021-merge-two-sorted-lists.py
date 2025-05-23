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
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list2: # list1 must be gone
            curr.next = list2
        else: # list2 must be gone
            curr.next = list1
        
        return head

"""
1 -> 2 -> 4
1 -> 3 -> 4
============

head = 1 ->.1 ->  ...
list1 = 2-> 4
list2 =  3 -> 4

curr = 1-> 1 ->...



"""