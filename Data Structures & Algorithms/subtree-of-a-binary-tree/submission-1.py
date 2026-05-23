# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if (root is None or subRoot is None) or root.val != subRoot.val:
            return False

        left_result = self.isSameTree(root.left, subRoot.left)
        right_result = self.isSameTree(root.right, subRoot.right)
        return left_result and right_result

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True        
        if root is None or subRoot is None:
            return False

        if self.isSameTree(root, subRoot):
            return True
            

        # 左側か右側かにsubtreeが見つかったらTrueを返す        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)