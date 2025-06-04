class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        suffix_product = 1
        for num in reversed(nums):
            suffix_product *= num
            result.append(suffix_product)
        result = list(reversed(result))
        prefix_product = 1
        for i, num in enumerate(nums[:-1]):
            result[i] = prefix_product * result[i+1]
            prefix_product *= num
        result[-1] = prefix_product
        return result

"""
ANKI
- First mention the division answer is easiest, provided you watch out for zeros as potholes"
** If more than one zero, then every output is 0.
** If exactly one zero, then only the position of that zero has non-zero product; all others are 0.
** If no zeros, you can compute the total product and divide.

- An O(n^2) solution is to take each element and multiply it over each element in the list, like a traversal, where every element takes turns

- If you want this to be O(n), precompute all prefixes and suffixes, and pair them together while avoiding
the current index.

- Lastly, if you want to use O(1) space, you should precompute either the prefixes or suffixes,
storing that in the array that you would have used as the return array anyway,
and the other (e.g. the prefixes) should "roll-up" in live time.


NOTES
[1,2,3,4]
[36,36,12,4]


Without using the division operation is harder because you could product everything together
and then divide out each anew respectively, while being mindful of factors with 0 as potholes

I think this is another party trick problem because you could do some leapfrog maneuver but
I suspect that'd deviate from O(n) time since you'd still be multiplying with each one
What I mean to say is that some sort of memoization or caching isn't going to work here
if you want to maintain O(n) time 

An O(n^2) solution is to take each element and multiply it over each element in the list, like a traversal
where every element takes turns

Well I guess Hint 1 in leetcode is that you can take the prefix and suffix and "roll them up" together
to get your products. Aka a prefix of length 1 is paired with a suffix of everything excluding that
and the index it's supposed to skip. In which case you get O(n) for the prefix rollup, O(n) for the suffix
rollup, and O(n) for doing all the pairings.

For the O(1) space complexity: "Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)"
This from leetcode is kind of a hint because it means that you could reuse the output array 
as a place to store either the prefixes or suffixes precomputed, and then do the pairings in live time.
If for some reason you needed extra space, you could overwrite the input array (but I don't see that
as necessary here).

"""
