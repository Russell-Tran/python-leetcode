class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_range = 0
        for i, capacity in enumerate(nums):
            if i > farthest_range:
                return False
            farthest_range = max(farthest_range, i+capacity)
            if farthest_range >= len(nums) - 1:
                return True
        return False

    



"""
nums = [2,3,1,1,4]
        ^   ^ ^

nums = [3,2,1,0,4]
        ^. ^  ^^


anchor = 0
        explorer = nums[0]

        for jump in reversed(range(nums[anchor]))

        def recurse()



if len(nums) == 1:
            return True
        
        invalids = set()

        def recurse(i: int) -> bool:
            if i in invalids:
                return False
            print("i = {}".format(i))
            for offset in reversed(range(1, nums[i] + 1)):
                jump_idx = i + offset
                if jump_idx >= len(nums) - 1 or recurse(jump_idx):
                    return True
            invalids.add(i)
            return False
        
        return recurse(i=0)
"""