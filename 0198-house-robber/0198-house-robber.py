class Solution:
    def rob(self, nums: List[int]) -> int:
        non_touch_optimals = [0]
        touch_optimals = [nums[0]]

        for num in nums[1:]:
            prev_optimal_touch = touch_optimals[-1]
            prev_optimal_non_touch = non_touch_optimals[-1]
            non_touch_optimals.append(max(prev_optimal_non_touch, prev_optimal_touch))
            touch_optimals.append(num + prev_optimal_non_touch)
            
        return max(non_touch_optimals[-1], touch_optimals[-1])



