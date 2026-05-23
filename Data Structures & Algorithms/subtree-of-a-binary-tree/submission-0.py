# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True        
        if root is None or subRoot is None:
            return False

        # 今の valが 一致するか否かをチェック
        # 一致したら：左と右をチェックする。
        # 一致しなかったら、rootのnodeを左と右にずらして確認
        if root.val != subRoot.val:
            left_looking = self.isSubtree(root.left, subRoot)
            right_looking = self.isSubtree(root.right, subRoot)
            return left_looking or right_looking
        else:
            left_looking = self.isSubtree(root.left, subRoot.left)
            right_looking = self.isSubtree(root.right, subRoot.right)
            

            # 左側か右側かにsubtreeが見つかったらTrueを返す        
            return left_looking and right_looking