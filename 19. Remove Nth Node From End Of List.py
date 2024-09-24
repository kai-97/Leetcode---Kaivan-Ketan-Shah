# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        slow = head
        counter = n

        while counter != 0:
            fast = fast.next
            counter -= 1
        
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return head
        
        
    
        
        
        
        
        
        
        # Earlier Try
        # if not head:
        #     return head

        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next
        
        # if length == 1:
        #     if n == 1:
        #         return None
        #     return head.next

        # remove_node = length-n+1

        # prev = None
        # curr = head
        # nex = curr.next

        # if remove_node == 1:
        #     return head.next
            
        # while remove_node != 1:
        #     print(curr.val)
        #     prev = curr
        #     curr = nex
        #     nex = curr.next
        #     remove_node -= 1

        # prev.next = nex

        # return head