class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)
        while lower < upper:
            midpoint = (upper + lower) // 2
            if target == nums[midpoint]:
                return midpoint
            elif target > nums[midpoint]:
                lower = midpoint + 1
            else:
                upper = midpoint
        return -1