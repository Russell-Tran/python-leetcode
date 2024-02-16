class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        duplicates_removed = 0
        
        trail_ptr = 1
        
        lead_ptr = 1
        recent_value = nums[0]
        times_seen = 1
        
        for i in range(1, len(nums)):
            lead_ptr = i
            if nums[i] == recent_value:
                if times_seen < 2:
                    nums[trail_ptr] = nums[lead_ptr]
                    trail_ptr += 1
                    times_seen += 1
                    continue
                else: # times_seen >= 2
                    duplicates_removed += 1
                    times_seen += 1
                    continue
            else:
                recent_value = nums[i]
                times_seen = 1
                nums[trail_ptr] = nums[lead_ptr]
                trail_ptr += 1
                continue
            
        k = len(nums) - duplicates_removed
        return k