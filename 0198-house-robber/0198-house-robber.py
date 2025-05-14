class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Here's my rationale:
        The choice to be made at each point, assuming we know the n-1 problem is solved,
        is whether this n array is better off in a touch-world or a non-touch world
        with this last element. That is, the touch-world is the optimal of the subproblem
        since we aren't going to include the last element. Likewise, the non-touch-world
        is the optimal of the subproblem + inclusion of the last element. 

        However, when we make this decision, we impact the future n+1 problem.
        Because if we choose to touch, then the future n+1 needs to know that. 
        And if we choose not to touch, the future n+1 also needs to know that.
        So we go and store that in separate arrays. Really it could just be variables
        but this is a bit nicer aesthetically for DP problems/debugging. (Really
        though the space complexity can just be O(1) instead of this O(n) because 
        we just need to store the last TOUCH and NON-TOUCH variables). 

        THAT IS,
        NEW TOUCH = this element + optimal of the immediate subproblem's NON-TOUCH
        NEW NON-TOUCH = max(immediate subproblem's NON-TOUCH, immediate subproblem's TOUCH)
                        ^ the max here is because by going non-touch, we want to pull 
                        forward the best of either worlds, since the NON-TOUCH world
                        is as valid as the TOUCH world, since the optimals of both
                        count as non-touching because the decision made at n was not to 
                        touch.

        Once we've filled out the arrays/run through the input,
        just return the max of the latest TOUCH and NON-TOUCH worlds.
        """


        non_touch_optimals = [0]
        touch_optimals = [nums[0]]

        for num in nums[1:]:
            prev_optimal_touch = touch_optimals[-1]
            prev_optimal_non_touch = non_touch_optimals[-1]
            non_touch_optimals.append(max(prev_optimal_non_touch, prev_optimal_touch))
            touch_optimals.append(num + prev_optimal_non_touch)
            
        return max(non_touch_optimals[-1], touch_optimals[-1])



