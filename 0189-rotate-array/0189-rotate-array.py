class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # ok this is a method where you don't care about memory cost
        
        output = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dest = (i + k) % len(nums)
            output[dest] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = output[i]
            
        return