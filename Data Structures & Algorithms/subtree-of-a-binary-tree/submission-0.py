# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def sameTree(self, treeA: Optional[TreeNode], treeB: Optional[TreeNode]) -> bool:
        if not treeA and not treeB:
            return True
        if treeA and treeB and treeA.val == treeB.val:
            return (self.sameTree(treeA.left,treeB.left) and self.sameTree(treeA.right,treeB.right))
        return False
        