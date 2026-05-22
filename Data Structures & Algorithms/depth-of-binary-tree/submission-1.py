# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        
        if root == None:
            return depth
                
        
        depth_left = depth_right = depth + 1

        if root.left != None:
            depth_left += self.maxDepth(root.left)
        if root.right != None:
            depth_right += self.maxDepth(root.right)

        return max(depth_left, depth_right)
