# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        point = len(arr) -n
        l = 0
        
        if len(arr) == 1 and n == 1:
            head.next = None
            head = head.next
            return head
        prev = ListNode(next=head)
        dummy = prev
        cur = head
        print(point)
        while l<=point:
            if l == point:
                prev.next = cur.next
                prev = prev.next
                cur = cur.next.next if cur.next else None
            else:
                prev.next = cur
                prev = prev.next
                cur = cur.next
            
            l+=1
        return dummy.next