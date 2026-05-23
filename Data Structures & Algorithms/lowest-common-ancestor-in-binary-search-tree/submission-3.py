# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isLeft(self, root: int , p: int , q: int):
        return p < root and q < root
    
    def isRight(self, root: int , p: int , q: int):
        return p > root and q > root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # どちらかのサイドにp,qに偏っている場合はLCAではないため次を探す。
        if self.isLeft(root.val, p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.isRight(root.val, p.val, q.val):
            return self.lowestCommonAncestor(root.right,p, q)
        
        # どちらかによっている場合は、LCAの候補となるため、対象のP,Qを探し当てる
        return root