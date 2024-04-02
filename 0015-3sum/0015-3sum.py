from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        
        tuples = set()
        for num in counts:
            counts[num] -= 1
            for othernum in counts:
                if counts[othernum] > 0:
                    counts[othernum] -= 1
                    if othernum >= num:
                        need = -1 * (num + othernum)
                        if need in counts and counts[need] > 0:
                            tuples.add(tuple(sorted([num, othernum, need])))
                    else:
                        pass
                    counts[othernum] += 1
            counts[num] += 1
            
        return [list(tup) for tup in tuples]
        
"""
[-1,0,1,2,-1,-4]


"""