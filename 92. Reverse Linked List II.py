# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head.next or left==right:
            return head

        curr = head
        prev = None
        rev_start = None
        rev_end = None
        i = 0
        while i != right:
            i += 1
            if i == left:
                p1 = prev
                rev_start = curr
            if i == right:
                rev_end = curr
            prev = curr
            curr = curr.next
        n2 = rev_end.next

        p = None
        c = rev_start
        n = c.next

        while c != rev_end:
            c.next = p
            p = c
            c = n
            n = c.next
        c.next = p
        rev_start.next = n2
        if not p1:
            return c
        p1.next = rev_end

        return head
        
