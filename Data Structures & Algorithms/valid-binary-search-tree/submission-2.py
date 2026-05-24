# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self, node, low, high):
        # ベースケース：node が None なら？（空の木 = 違反なし）
        if node is None:
            return True
        
        # 値のチェック：low < node.val < high を満たしてるか？
        # 満たしてなければ False
        if low >= node.val or high <= node.val:
            return False
        
        # 左の子に再帰：何を low、何を high で渡す？（質問3の答え）
        left_check = self.validate(node.left, low, node.val)
        # 右の子に再帰：何を low、何を high で渡す？（質問4の答え）
        right_check = self.validate(node.right, node.val, high)

        # 両方 True なら全体 True
        return left_check and right_check

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))