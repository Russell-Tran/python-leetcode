# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        dummy = ListNode(-1)
        dummy.next = head

        first = dummy
        second = dummy

        while first and second:
            first = first.next
            second = second.next
            if not second:
                break
            second = second.next
            if first == second:
                return True
        
        return False

"""



"""