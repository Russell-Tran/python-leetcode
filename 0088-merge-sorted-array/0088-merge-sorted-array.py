class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        builder_idx = len(nums1) - 1
        first_list_idx = m - 1
        second_list_idx = n - 1

        while builder_idx >= 0:
            if second_list_idx < 0 or (first_list_idx >= 0 and nums1[first_list_idx] >= nums2[second_list_idx]):
                nums1[builder_idx] = nums1[first_list_idx]
                first_list_idx -= 1
            else:
                nums1[builder_idx] = nums2[second_list_idx]
                second_list_idx -= 1
            builder_idx -= 1

        return





        # i, j, k = 0, 0, 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums[i] <= nums[j]:
        #         # ignore
        #         i += 1
        #     else:
        #         temp = nums[i]
        #         nums[i] = nums[j]
        #         nums[j] = temp
