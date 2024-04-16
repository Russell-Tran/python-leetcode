class Node:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def add_to_tree(self, root, datum):
        val = datum % 10
        datum //= 10
        position = datum % 10
        datum //= 10
        depth = datum
    
        cur = root
        if depth == 4:
            if 1 <= position and position <= 4:
                cur = cur.left
            else:
                # 5 <= position <= 8
                cur = cur.right
                position -= 4
            depth -= 1
            
        if depth == 3:
            if 1 <= position and position <= 2:
                cur = cur.left
            else:
                # 3 <= position <= 4
                cur = cur.right 
                position -= 2
            depth -= -1
            
        # depth is now 2
        if position == 1:
            cur.left = Node(val)
        else:
            # position == 2
            cur.right = Node(val)
        
    def recurse(self, root, soFar=0):
        soFar += root.val
        
        if not root.left and not root.right:
            self.sum += soFar
            
        if root.left:
            self.recurse(root.left, soFar)
            
        if root.right:
            self.recurse(root.right, soFar)
    
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Sort to prevent orphans
        nums = sorted(nums)
        
        # Pop off head
        root_data = nums[0]
        nums = nums[1:]
        
        # Make root
        val = root_data % 10
        root = Node(val)
        
        # Build the rest of the tree
        for datum in nums:
            self.add_to_tree(root, datum)
            
        # Recursive backtrack to accumulate a sum of paths
        self.sum = 0
        self.recurse(root)
        return self.sum