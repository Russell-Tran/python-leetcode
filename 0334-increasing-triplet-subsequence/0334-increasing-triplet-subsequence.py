import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        collections = []
        for num in nums:
            placed = False
            for collection in collections:
                if num < collection[-1]:
                    if len(collection) < 2 or num > collection[-2]:
                        collection[-1] = num
                        placed = True
                    elif num == collection[-2]:
                        placed = True
                elif num > collection[-1]:
                    collection.append(num)
                    placed = True
                else:
                    placed = True
            if not placed:
                collections.append([num])
        for collection in collections:
            if len(collection) >= 3:
                return True
        return False
        