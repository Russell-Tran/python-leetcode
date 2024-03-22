class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        all1 = set(nums1)
        all2 = set(nums2)
        answer = [all1 - all2, all2 - all1]
        return answer