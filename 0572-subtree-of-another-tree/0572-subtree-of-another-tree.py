# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def trees_match(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            return bool(p and q and p.val == q.val and trees_match(p.left, q.left) and trees_match(p.right, q.right))

        def discover_roots(node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node and node.val == subRoot.val and trees_match(node, subRoot):
                return True
            if discover_roots(node.left, subRoot):
                return True
            if discover_roots(node.right, subRoot):
                return True
            return False

        return discover_roots(root, subRoot)



"""
ideas: traverse downward and rebuild a tree (identify a subtree)
because based on leaves
i think also you could do a recurse search where you DFS (want to prioritize likelihood of leaves) until you find a val matchup, then do a tree comparison 
sort of depends if you want to discover all roots first or bet on the first valid root that you see 
i think it's easier to implement first valid root you see,
then later we can consider what needs to be done for efficiency of 
collecting all the roots, which might be more efficient 
"""