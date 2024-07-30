# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2

        head = ListNode(-1)
        result = head
        carry = 0
        while curr1 and curr2:
            total_sum = curr1.val + curr2.val + carry
            result.next = ListNode(total_sum%10)
            carry = total_sum // 10

            curr1 = curr1.next
            curr2 = curr2.next
            result = result.next
        
        while curr1:
            total_sum = curr1.val + carry
            result.next = ListNode(total_sum%10)
            carry = total_sum//10
            curr1 = curr1.next
            result = result.next
        
        while curr2:
            total_sum = curr2.val + carry
            result.next = ListNode(total_sum%10)
            carry = total_sum//10
            curr2 = curr2.next
            result = result.next

        if carry:
            result.next = ListNode(carry)

        return head.next