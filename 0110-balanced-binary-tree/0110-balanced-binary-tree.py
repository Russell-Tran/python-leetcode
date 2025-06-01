# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # returns if balanced, and the height
        def recurse(node: Optional[TreeNode]) -> (bool, int):
            if not node:
                return True, -1
            left_is_balanced, left_height = recurse(node.left)
            if not left_is_balanced:
                return False, 0
            right_is_balanced, right_height = recurse(node.right)
            if not right_is_balanced:
                return False, 0
            height_difference = abs(left_height - right_height)
            if height_difference > 1:
                return False, 0
            return True, 1 + max(left_height, right_height)
        
        return recurse(root)[0]
            
            

            
