# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 子要素を集める
        # ステップ1: 結果を入れる箱（空リスト）
        return_list_nodes = []
        
        # ステップ2: current_level = [root] で初期化
        current_level = [root] if root else []
        
        # ステップ3: while ループ
        while current_level:
            elm_list = []
            next_level = []
            # (A) 今のレベルの「値」を集めて、結果に追加
            for node in current_level:
                elm_list.append(node.val)

                # (B) 今のレベルの各ノードの「子供」を集めて next_level を作る
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
                
            # (C) current_level = next_level で更新
            current_level = next_level
            return_list_nodes.append(elm_list)
 
        return return_list_nodes


        