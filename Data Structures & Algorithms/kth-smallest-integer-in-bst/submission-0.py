# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node, result):
        if not node:
            return

        self.inorder(node.left, result)   # 左を全部訪れる

        # ここで node.val を処理する
        result.append(node.val)

        self.inorder(node.right, result)  # 右を全部訪れる


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # result = [] を用意
        result = []
        # inorder を呼ぶ
        self.inorder(root, result)
        # result[k-1] を返す
        return result[k-1]
        

            



        