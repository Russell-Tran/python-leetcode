class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        nums = sorted(nums)
        #print("nums = {}".format(nums))
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                # We do this because the point of i is to be unique
                # THIS SAVES RUNTIME
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                #print("i = {}, j = {}, k =  {}".format(i, j, k))
                #print("combo = {}, {}, {}".format(nums[i], nums[j], nums[k]))
                # if j - i > 2 and j > 1 and nums[j] == nums[j-1] == nums[j-2]:
                #     j += 1
                #     continue
                # if k < len(nums) - 2 and nums[k] == nums[k+1] == nums[k+2]:
                #     k -= 1
                #     continue
                # if j - i > 2 and nums[j] == nums[j-i] and k - j > 1:
                #     j += 1
                #     continue

                # if k < len(nums) - 1 and nums[k] == nums[k+1]:
                #     k -= 1
                #     continue WEIRD BUT SOME REASON THIS ACTUALLY INCREASES RUNTIME

                summation = nums[i] + nums[j] + nums[k]
                if summation == 0:
                    #result.append([nums[i], nums[j], nums[k]])
                    solutions.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif summation < 0:
                    j += 1
                else:
                    k -= 1
        return [list(solution) for solution in solutions]

"""
ANKI 
- Okay so apparently the only way to solve this is to remember Two Sum and Two Sum II solutions
and build off that (like the interviewer will upgrade either to 3sum)

- If using Two Sum II, or just remembering it, you can go ahead and sort this input. Then,
iterating over i and holding it constant, do the increment the left if sum is too small (less than zero)
and decremenet the right if sum is too big (greater than zero). If the previous i element is the same,
you can skip it. But the left and right i haven't figured out how to skip, so just store everything
as tuples for now in a hashset and convert it at the end to get unique values. 
[[TODO: figure out how to not rely on the hashset of tuples]]

- [[TODO: NEED TO DO THE Two Sum problem first]]

DEBUG
[-1,0,1,2,-1,-4]
i = 0
j = 1
k = 2
sorted = [-4 -1 -1 0 1 2]


========
[0 0 0]
for i in [0]:

i = 0
j = 1
k = 2

1 < 2:
summation = 0


NOTES
Ok so, 
Since i just did the Two Sum II where input array is sorted,
i can think of a O(n^2) answer

and this is better than an O(n^3) answer which is brute force every combo to see if it matches

so basically, start by sorting the array, which takes O(n log n) time

Then do a O(n) traversal of the array, and basically within each iteration of that loop,
bounded by wherever that first index i is,
we do a two pointer search of counterparts, 
so the idea is that, bounded by the lower on i,
we have a j and k who , the j starts left and the k starts right
and whenever the element at j + element at k is too high, decrement the k
and whenever the elemenet at j + element at k is too low, increment the j
and whenever there's a target hit, save the triplet index

the way you ensure there's no duplicate triplets is because that i is like the
floor that is raising each time, so there's no way for anyone to accidentally go 
back and include that i 
(right like in proof land the definition of unique is that there's at least one
elemente in there that for sure isn't in any of the others)

and of course, this goes without saying, but holding a given i fixed the j and k
are unique because we're squeezing

ALSO, we need a mechanism to avoid duplicate in i-land and duplicates in j and k land
the answer to i-land is that if the prev element is the same, we skip it
the answer to j-and-k land is that if the prev for either is the same, we skip it
(check each and move the offender). can use a simple boolean flag or a recompute
that the previous elements sum to the target, but honestly that's overkill.
just check that your prev of YOU is a duplicate, since that means we already have our answer
for that, regardless of whether that was a solution or not, and move on.



HONESTLY , maybe the easiest way to avoid duplicates is just have a set
because this ^^^^^ stuff to avoid duplicates didn't even work:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        #print("nums = {}".format(nums))
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                #print("i = {}, j = {}, k =  {}".format(i, j, k))
                #print("combo = {}, {}, {}".format(nums[i], nums[j], nums[k]))
                if j - i > 2 and j > 1 and nums[j] == nums[j-1] == nums[j-2]:
                    j += 1
                    continue
                if k < len(nums) - 2 and nums[k] == nums[k+1] == nums[k+2]:
                    k -= 1
                    continue
                summation = nums[i] + nums[j] + nums[k]
                if summation == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif summation < 0:
                    j += 1
                else:
                    k -= 1
        return result


YES and apparently the sets thing worked, though it made the runtime super slow idk why

"""