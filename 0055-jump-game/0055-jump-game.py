class Solution:
    
    
    def recurse(self, nums, idx) -> bool:
        # Base cases
        if idx == len(nums) - 1:
            return True
        
        jump_maximum = nums[idx]
        if jump_maximum == 0:
            return False
        
        # Explore 
        for jump in range(1, jump_maximum+1):
            candidate = idx + jump
            if candidate not in self.blacklist and self.recurse(nums, candidate):
                return True
            
        self.blacklist.add(idx)
        return False
            
    
    def canJump(self, nums: List[int]) -> bool:
        
        # It seems like you can use DFS
        self.blacklist = set()
        return self.recurse(nums, 0)
        