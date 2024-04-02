# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root):
        # if null do nothong
        if not root:
            return
        
        
        left = root.left
        right = root.right
        
        if not root.val in self.to_delete:
            if root.left and root.left.val in self.to_delete:
                root.left = None
            if root.right and root.right.val in self.to_delete:
                root.right = None
        else:
            # add each if they qualify
            if root.left and not root.left.val in self.to_delete:
                self.result.append(root.left)
            else:
                root.left = None
                
            if root.right and not root.right.val in self.to_delete:
                self.result.append(root.right)
            else:
                root.right = None
            
        # recurse on each child
        self.recurse(left)
        self.recurse(right)
            
        

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        self.result = []
        self.to_delete = set(to_delete)
        
        
        left = root.left
        right = root.right
        if not root.val in self.to_delete:
            self.result.append(root)
            self.recurse(root)
        else:
            # add each if they qualify
            if root.left and not root.left.val in self.to_delete:
                self.result.append(root.left)
            else:
                root.left = None
                
            if root.right and not root.right.val in self.to_delete:
                self.result.append(root.right)
            else:
                root.right = None
                
                
            self.recurse(left)
            self.recurse(right)
            
        return self.result
    
    