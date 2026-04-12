# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        cur1 = p
        cur2 = q
        while cur1 or cur2:
            while cur1:
                if not cur2:
                    return False
                if cur1.val != cur2.val:
                    return False
                stack1.append(cur1)
                stack2.append(cur2)
                cur1 = cur1.left
                cur2 = cur2.left
            if stack1 or stack2:
                cur1 = stack1.pop()
                cur2 = stack2.pop()
                cur1 = cur1.right
                cur2 = cur2.right
        return True
                