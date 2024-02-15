class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # identify all the indices of the duplicates
        duplicate_idxs = []
        last_unique_element_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last_unique_element_val:
                duplicate_idxs.append(i)
            else:
                last_unique_element_val = nums[i]
                    
        # do a shifting-down mechanism using the array of duplicate indices as a guide
        num_jumps = 0
        for i in range(1, len(nums)):
            if num_jumps < len(duplicate_idxs):
                if i < duplicate_idxs[num_jumps]:
                    nums[i - num_jumps] = nums[i]
                elif i == duplicate_idxs[num_jumps]:
                    pass
                else: # i > duplicate_idxs[num_jumps]
                    num_jumps += 1
                    nums[i - num_jumps] = nums[i]
            else:
                nums[i - num_jumps] = nums[i]
            
        
        # return k : # the number of unique is subtracting the number of duplicates
        return len(nums) - len(duplicate_idxs)