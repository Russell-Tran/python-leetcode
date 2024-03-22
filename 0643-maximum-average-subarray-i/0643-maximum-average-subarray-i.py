class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
        
        i = 0
        current_average = sum(nums[:k]) / k
        result = current_average
        while i + k < len(nums):
            current_average -= nums[i] / k
            current_average += nums[i+k] / k
            result = max(result, current_average)
            i += 1
        return result