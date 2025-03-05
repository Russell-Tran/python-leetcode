class Solution:


    def recurse(self, nums, target_idx):
        if target_idx == 0:
            return 0
        for i in range(target_idx):
            if i + nums[i] >= target_idx:
                return 1 + self.recurse(nums, i)
        
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        
        return self.recurse(nums, len(nums)-1)

        
    """
    JUNK
    # def recurse(self, nums, i, depth):
    #     if i >= len(nums) - 1:
    #         return depth

    #     depth += 1
    #     options = list(reversed(range(1, nums[i] + 1)))
    #     if not options:
    #         return float('inf')
    #     else:
    #         return min([self.recurse(nums, i + option, depth) for option in options])

    # def jump(self, nums: List[int]) -> int:
    #     if not nums or len(nums) == 1:
    #         return 0
    #     return self.recurse(nums, 0, 0)
    """