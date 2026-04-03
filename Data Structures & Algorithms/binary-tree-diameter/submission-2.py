# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = [0]
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            height_l = height(root.left)
            height_r = height(root.right)
            curr_diam = height_l + height_r
            max_diam[0] = max(max_diam[0], curr_diam)
            return 1 + max(height_l, height_r)
        max_height = height(root)
        return max_diam[0]