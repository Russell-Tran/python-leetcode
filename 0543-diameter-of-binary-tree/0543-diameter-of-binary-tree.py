# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self._recurse(root)) - 1 # subtract one because we've been counting nodes but we need to count edges
    
    def _recurse(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (0, 0)
        
        deepest_left_bridge, deepest_left_arm = self._recurse(root.left)
        deepest_right_bridge, deepest_right_arm = self._recurse(root.right)

        finalized_bridge = max(deepest_left_arm + 1 + deepest_right_arm, deepest_left_bridge, deepest_right_bridge)
        deepest_arm = max(deepest_left_arm, deepest_right_arm) + 1

        return (finalized_bridge, deepest_arm)
"""
Idea: deepest right + deepest left ("finalized bridge")
vs. deepest right OR left for propagation up the tree
"""