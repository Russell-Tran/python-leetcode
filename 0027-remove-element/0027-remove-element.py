class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        back_idx = len(nums) - 1
        i = 0
        count = 0
        
        while back_idx >= 0 and nums[back_idx] == val:
            back_idx -= 1
            count += 1
        while i < len(nums) and i < back_idx:
            if nums[i] == val:
                count += 1
                nums[i] = nums[back_idx]
                back_idx -= 1
                while back_idx >= 0 and nums[back_idx] == val:
                    back_idx -= 1
                    count += 1
            i += 1
            
        k = len(nums) - count
        return k