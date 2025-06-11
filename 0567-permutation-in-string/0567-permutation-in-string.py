from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        requirements = Counter(s1)
        left_idx, right_idx = 0, len(s1)
        candidate = Counter(s2[:right_idx])

        while right_idx < len(s2):
            #print("requirements = {}, candidate = {}".format(requirements, candidate))
            if requirements == candidate:
                return True
            #print("left_idx = {}, right_idx = {}".format(left_idx, right_idx))
            left, right = s2[left_idx], s2[right_idx]
            candidate[left] -= 1
            candidate[right] += 1
            left_idx += 1
            right_idx += 1

        # Check for the last time
        if requirements == candidate:
                return True
        return False
"""
Well something like this looks like you just 
get the char counts of each
then check that all the counts are <= to the "superset's" counts

Actually no this problem is harder than that

actually not too bad, yeah just char counts it 

"""