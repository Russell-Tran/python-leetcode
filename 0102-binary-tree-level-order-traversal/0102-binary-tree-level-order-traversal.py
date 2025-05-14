# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        Initial thoughts:
        This looks like BFS - BFS works well with a queue
        """
        if not root:
            return []

        result = []
        package = []
        queue = deque([root, None]) # None is a boundary marker here
        while queue:
            node = queue.popleft()
            if node is None: # create the beautiful little packages
                result.append(package)
                package = []
                continue

            package.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if len(queue) > 1 and queue[0] is None:
                queue.append(None) # add back a marker only if we've finished the level

        return result

        """
        NOTE: ChatGPT would rather you keep track of the length of each level
        by measuring the length of the queue before each round;
        it's more elegant that way and you don't need markers
        or this wonky de-deuplication of markers if len(queue) > 1 and queue[0] is None:
        because len(queue) > 1 is my way of avoiding an extra empty package at the end
        """
        