class Solution:
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        zero_anchor = 0
        front_runner = 0
        
        # get the first zero
        while zero_anchor < len(nums) and nums[zero_anchor] != 0:
            zero_anchor += 1
            
        # get the first nonzero after the first zero
        front_runner = zero_anchor
        while front_runner < len(nums) and nums[front_runner] == 0:
            front_runner += 1
        
        while zero_anchor < len(nums) and front_runner < len(nums):
            # swap
            nums[zero_anchor] = nums[front_runner]
            nums[front_runner] = 0
            
            # traverse
            while zero_anchor < len(nums) and nums[zero_anchor] != 0:
                zero_anchor += 1
            while front_runner < len(nums) and nums[front_runner] == 0:
                front_runner += 1
        return
       
        

        
        