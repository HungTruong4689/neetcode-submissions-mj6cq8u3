# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        s1 = ""
        s2 = ""
        while cur1:
            s1 += str(cur1.val)
            cur1 = cur1.next
        while cur2:
            s2 += str(cur2.val)
            cur2 = cur2.next
        s = int(s1[::-1]) + int(s2[::-1])
        m = str(s)[::-1]
        print(m)
        dummy = ListNode(0)
        cur = dummy
        for i in m:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next