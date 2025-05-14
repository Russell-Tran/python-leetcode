class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            
            # implies minimum is to the right because it looped
            if nums[mid] > nums[high]:
                low = mid + 1

            # implies minimum is to the left, because of the
            # absence of the looping behavior
            else:
                high = mid
        
        return nums[low] # convergence