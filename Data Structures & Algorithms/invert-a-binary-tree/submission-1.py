# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        if current != None and (current.left != None or current.right != None):
            current.left, current.right = current.right, current.left
            if current.left != None:
                self.invertTree(current.left)
            if current.right != None:
                self.invertTree(current.right)
        return root