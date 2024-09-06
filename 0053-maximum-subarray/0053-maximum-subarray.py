class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        
#         def has_positive(nums) -> bool:
#             for num in nums:
#                 if num > 0:
#                     return True
#             return False
        
#         if not has_positive(nums):
#             return max(nums)
        
    
        # keep a running tab
        # keep track of the best summation
        
        # you are a snake
        # grow through the seasons until you hit a negative then positive season
        # (any time you grow you should compare against the best summation)
        # then ask yourself whether you come out ahead
        # if you don't come out ahead, then cut off your tail and start anew
        
        best_summation = max(nums)
        current_summation = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i-1] < 0 and nums[i] >= 0: 
                if current_summation < 0:
                    current_summation = 0
                    
            current_summation += nums[i]
            best_summation = max(best_summation, current_summation)
            
        return best_summation