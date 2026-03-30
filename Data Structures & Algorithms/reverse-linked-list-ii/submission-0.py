# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
        arr = arr[:left-1] + arr[left-1:right][::-1] + arr[right:]
        print(arr)
        node = ListNode()
        cur = node
        for i in arr:
            newNode = ListNode(i)
            cur.next = newNode
            cur = cur.next
        return node.next