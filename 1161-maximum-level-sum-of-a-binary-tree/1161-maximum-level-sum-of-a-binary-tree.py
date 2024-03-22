# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        best_level = 1
        best_sum = root.val
        
        root.level = 0
        
        queue = [root]
        current_level = 1
        current_sum = 0
        while queue:
            node = queue[0]
            queue = queue[1:]
            
            # signifies that we're at the next level
            if node.level > current_level:
                if current_sum > best_sum:
                    best_level = current_level
                    best_sum = current_sum
                current_level = node.level
                current_sum = 0
                
            current_sum += node.val
            if node.left:
                node.left.level = current_level + 1
                queue.append(node.left)
            if node.right:
                node.right.level = current_level + 1
                queue.append(node.right)
        
        # don't forget about the last level!
        if current_sum > best_sum:
            best_level = current_level
            best_sum = current_sum
            
        return best_level
        
            