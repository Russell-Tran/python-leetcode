class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1
"""
ANKI
- O(n^2) solution would be to do a nested for-loop and for each element, re-iterate over
everyone else to find the counterpart 

- O(n log n) solution would be to iterate over the array, and for each, do a binary search
for the counterpart 

- PARTY TRICK: O(n) solution is to put a pointer at the bottom and a pointer at the top.
What you do is assume one of the two elements is part of the solution.
If the left one is part of the solution, then either the right is also part of the solution
or the sum is too high. In which case keep decrementing the index of the right until you find it.
However, if the sum is too low, the left can't possibly be part of the solution, because there's
no counterpart that's possibly big enough to meet its needs.

Similarly, if the right one is part of the solution, then either the left one is also part 
of the solution, or the sum is too low. In which case keep incrementing the index of the left
until you find it. However, if the sum is too high, the right can't possibly be part of the solution,
because there's no counterpart that's possibly low enough to meet its needs.

SO BASICALLY: Start the left at the start, and the right at the end. 
If sum > target: right -- (this left index *could* still be a solution if only the right were smaller)
If sum < target: left ++ (this right index *could* still be a solution if only the left were bigger)
If sum == target: return two indices

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

WELL THIS WAS MY BINARY SEARCH SOLN
which worked but is O(n log n) instead of O(n) so :

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