# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output_pre_head = ListNode()
        output_curr = output_pre_head
        
        carry = 0
        
        l1_curr = l1
        l2_curr = l2
        
        while l1_curr or l2_curr:
            child = ListNode()
            child.val += carry
            if l1_curr:
                child.val += l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr:
                child.val += l2_curr.val
                l2_curr = l2_curr.next
            carry = child.val // 10
            child.val = child.val % 10
            output_curr.next = child
            output_curr = output_curr.next
        if carry > 0:
            output_curr.next = ListNode(carry)
        return output_pre_head.next
            