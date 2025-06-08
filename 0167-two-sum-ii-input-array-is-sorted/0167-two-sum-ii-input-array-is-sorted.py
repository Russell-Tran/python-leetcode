class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def format(i, j):
            return [i+1, j+1]

        for i, number in enumerate(numbers):
            counterpart = target - number
            low = i + 1
            high = len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == counterpart:
                    return format(i, mid)
                elif numbers[mid] < counterpart:
                    low = mid + 1
                else:
                    high = mid - 1
"""
NOTES
already sorted in non-decreasing order

find two numbers that add up to a specific target

return the 2 indices 1-indexed 

cannot use same element twice

must use only constant extra space

I think the INSIGHT might be about , since it's in non-decreasing order, 
you'll know quickly that a counterpart no longer exists 

or the two pointers approach, come from the back to find the counterpart 

well there's also the possibility of binary search 

O(n^2) solution would be to do a nested for-loop and for each element, re-iterate over
everyone else to find the counterpart 

O(n log n) solution would be to iterate over the array, and for each, do a binary search
of the counterpart 

"""