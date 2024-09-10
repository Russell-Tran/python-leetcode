class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left_ptr, right_ptr = 0, len(numbers) - 1
        
        while left_ptr != right_ptr:
            left = numbers[left_ptr]
            right = numbers[right_ptr]
            summation = right + left
            
            if summation == target:
                break
            elif summation < target:
                left_ptr += 1
            else: # summation > target
                right_ptr -=1
        
        return [left_ptr + 1, right_ptr + 1]