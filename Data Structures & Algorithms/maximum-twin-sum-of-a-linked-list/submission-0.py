# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        m =0
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next
        n = len(stack)
        for i in range(int(n/2)):
            m = max(m,stack[i]+ stack[n-1-i])

        return m

