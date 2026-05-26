# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def dfs(node):
            if not node:
                return
            val = node.val
            if low <= val and val <= high:
                res.append(val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return sum(res)
            
            
            