# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        cur1 = l1
        cur2 = l2
        while cur1:
            s1 += str(cur1.val)
            cur1 = cur1.next
        while cur2:
            s2 += str(cur2.val)
            cur2 = cur2.next

        res = str(int(s1)+ int(s2))
        dummy = ListNode(0)
        cur = dummy
        for i in res:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return dummy.next