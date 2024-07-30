# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        k = k%n
        if k == 0:
            return head

        new_end = head
        for i in range(n-k-1):
            new_end = new_end.next
        
        new_head = new_end.next
        new_end.next = None

        to_end = new_head
        while to_end.next:
            to_end = to_end.next
        to_end.next = head

        return new_head