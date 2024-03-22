# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right
    
    def recurse(self, lineup, node):
        if not node:
            return
        
        if self.isLeaf(node):
            if lineup == '1':
                self.lineup1.append(node.val)
            else:
                self.lineup2.append(node.val)
            return
        
        self.recurse(lineup, node.left)
        self.recurse(lineup, node.right)
        
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.lineup1 = []
        self.lineup2 = []
        self.recurse('1', root1)
        self.recurse('2', root2)
        return self.lineup1 == self.lineup2
    