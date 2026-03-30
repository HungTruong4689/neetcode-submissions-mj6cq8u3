# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Find the length and the old tail
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # 2. Close the loop (make it circular)
        old_tail.next = head
        
        # 3. Find the new tail: (length - k % length - 1) nodes from the start
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 4. Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head