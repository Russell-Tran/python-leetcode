class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        best = 0
        while i < j:
            left, right = height[i], height[j]
            area = min(left, right) * (j - i)
            best = max(best, area)
            if left < right:
                i += 1
            else:
                j -= 1
        return best

"""
ok so it's a two pointers one so
it's something like
put the left and right pointers as far as possible
you step 1 away from whichever stick is smaller, since that one's "volume" (area)
is already tapped out at this point, like that's the most it's ever gonna be,
so you should compare it against the best so far
The two pointers ensure a O(n) traversal too. 
return the best

"""