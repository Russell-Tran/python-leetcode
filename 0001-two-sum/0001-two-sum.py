class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in nums[i+1:]:
                diff_idx = nums.index(diff, i+1)
                return [i, diff_idx]