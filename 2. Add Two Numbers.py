# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2, head2 = l2, l2
        carry = 0
        prev1, prev2 = None, None

        while curr1 and curr2:
            su = curr1.val + curr2.val + carry
            carry = su//10
            remainder = su%10

            curr2.val = remainder
            prev1, prev2 = curr1, curr2
            curr1, curr2 = curr1.next, curr2.next
        
        prev = prev2 if prev2 else None
        if curr1 or curr2:
            if curr1:
                prev2.next = curr1
                curr2 = prev2.next
            while curr2:
                su = curr2.val + carry
                carry = su//10
                remainder = su%10

                curr2.val = remainder
                prev, curr2 = curr2, curr2.next
        
        if carry:
            prev.next = ListNode(1)
        return head2