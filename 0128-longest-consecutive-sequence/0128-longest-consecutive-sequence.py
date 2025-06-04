class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums) # O(n)

        consecutive_runs = {} # start inclusive -> stop exclusive
        reverse_reference = {} # stop exclusive -> start inclusive

        for num in nums: # O(n) with O(1) operations inside
            # check if you can stick to a sequence run immediately following you
            if num + 1 in consecutive_runs:
                stop = consecutive_runs[num + 1]
                del consecutive_runs[num + 1]
                consecutive_runs[num] = stop
                reverse_reference[stop] = num
            # ELSE IF check if you can stick to a sequence run immediately preceding you
            # (AVOID DOUBLE DIPPING OR WILL CAUSE CONNECTION PROBLEMS LATER)
            elif num in reverse_reference:
                start = reverse_reference[num]
                consecutive_runs[start] = num + 1
                del reverse_reference[num]
                reverse_reference[num + 1] = start
            # ELSE create a new baby sequence run (seed crystal)
            else:
                consecutive_runs[num] = num + 1
                reverse_reference[num + 1] = num

        # NOW MERGE contiguous runs O(n)
        origins = set((start, stop) for start, stop in consecutive_runs.items())

        while origins:
            start, stop = origins.pop()
            while stop in consecutive_runs or start in reverse_reference:
                print("OUR CHUNK: {}->{}".format(start, stop))
                print("consecutive_runs = {}".format(consecutive_runs))
                print("reverse_reference = {}".format(reverse_reference))
                # our chunk precedes
                if stop in consecutive_runs:
                    their_start = stop
                    their_stop = consecutive_runs[their_start]

                    origins.remove((their_start, their_stop))

                    consecutive_runs[start] = their_stop
                    del consecutive_runs[their_start]

                    reverse_reference[their_stop] = start
                    del reverse_reference[stop]

                    stop = their_stop
                
                print("OUR CHUNK: {}->{}".format(start, stop))
                print("consecutive_runs = {}".format(consecutive_runs))
                print("reverse_reference = {}".format(reverse_reference))
                # our chunk follows (also allowed)
                if start in reverse_reference:
                    their_stop = start
                    their_start = reverse_reference[their_stop]
                    print("their_start = {} their_stop = {}".format(their_start, their_stop))

                    origins.remove((their_start, their_stop))
                    
                    consecutive_runs[their_start] = stop
                    del consecutive_runs[start]

                    reverse_reference[stop] = their_start
                    del reverse_reference[their_stop]

                    start = their_start

        # GET THE LONGEST RUN O(n)
        return max([stop - start for start, stop in consecutive_runs.items()])

"""
ANKI

NOTES
Length of the longest consecutive elements sequence
O(n) time


nums = [100,4,200,1,3,2]
[1, 2, 3, 4]
result should be 4 then

ideas:
could use sets somehow, to check efficiently that the next element is there

sorting isn't going to work because that's O(n log n) and we're required to do O(n)

could use sets or perhaps dictionaries to point around to jump around

there's also the notion of "capturing" intervals, like maintaining tuples floating
around that allow you to link contiguous sequences together.
even if you needed to glue the tuples together at the end, one at a time, you'd stay within
O(n)

i think something similar to that would work, i think you could grow icicles bidirectionally
using a dictionary.

>>> though we'd need to account for duplicates (DUPLICATE ELEMENT VALUES IN THE ORIGINAL ARRAY) to avoid weird duplicate icicles, easy just use a set

Icicles [start, stop): use this to check +1
100-> 101
4-> 5 BECOMES 3->5
200-> 201
1->2

Reverse boundaries (stop, start]: use this to check -1
101->100
5->4
201->200
2->1

It's completely acceptable to merge the crystals at the end. BUT THEN that begs whether
we should just deal with a setified list first (nah). I think the set conversion may make
things harder because you need to discriminate what you've seen before to avoid the
duplicates. Actually, looking above i need to convert the list to set. I just meant,
we should wait to merge crystals at the end rather than during flight.

"""