class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        partners = {} # value -> partner's idx
        for i, num in enumerate(nums):
            if num in partners:
                return [i, partners[num]]
            partner_val = target - num
            partners[partner_val] = i
        