class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1 # inclusive
        while lower <= upper: # inclusive
            midpoint = (lower + upper) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                lower = midpoint + 1
            else:
                upper = midpoint - 1
        return -1