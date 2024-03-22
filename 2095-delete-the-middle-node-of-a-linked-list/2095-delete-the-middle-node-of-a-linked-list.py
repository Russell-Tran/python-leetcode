# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = head
        slow = head
        prev = head
        i = 0
        while fast:
            i += 1
            if i > 0 and i % 2 == 0:
                prev = slow
                slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return head