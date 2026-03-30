# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        n = len(arr)//2 +1
        newArr = [0]* len(arr)
        l,r = 0, len(arr)-1
        for i in range(len(arr)):
            if i %2 ==0:
                newArr[i]= arr[l]
                l+=1
            else:
                newArr[i]= arr[r]
                r-=1
        print(arr,newArr)
       
        cur = head
        for i in newArr:
            
            cur.val = i
            cur = cur.next

        