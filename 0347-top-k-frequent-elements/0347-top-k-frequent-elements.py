import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for element in nums:
            counts[element] += 1

        heap = []
        for element, freq in counts.items():
            datum = (freq, element)
            if len(heap) < k:
                heapq.heappush(heap, datum)
            elif freq > heap[0][0]:
                heapq.heappushpop(heap, datum)
            
        return [datum[1] for datum in heap]

"""
ANKI
- count all them first  (NO NEED TO COUNT AS YOU GO), O(n)
- a size-limited heap is efficient since the inserts will be O(log k) each
- therefore you can do a O(n log k) which is more efficient than sorting in 
the absence of a heap which would be the dreaded O(n log n)
"""

"""
JUNK 2.0
- tricky: seems you need to track/finalize all the counts before you actually know who's in the top k of stats frequency

- inefficient idea: start with a dictionary that keeps counts; then the naive next step would be to sort that for the top k (problem with this is the space becomes n and the sorting is n log n)

- the only thing better than O(n log n ) here is O(n) because you have to iterate through the whole list. hypothetically speaking i mean to say we have a compute of at least O(n) for any solution

- so what we'd do is maintain a dictionary of counts , and each time just force-update a tuple record of that through a limited size heap aka a k-sized heap. And a push+pop is O(log k) + O(log k) = O(log k). This tuple record is smarter than trying to find the old tuple record and updating it. it seems weird because if you had a sequential of e.g. 5 5 5 5 5 5 that it might spam out the other ones, but actually we still keep the true ledger of frequencies, and anyone with a higher frequency is guaranteed to survive the spam

JUNK
- use a Heap : because efficient insertion and removal at O(log n), and consistent O(1) access to a max or min
- maybe something like a tuple that is led by the frequency and also carries the element


BAD BECAUSE YOU NEED TO COUNT FIRST OR ELSE - ALSO THIS GATEKEEPING FOR THIS ONE IS WRONG LOL
gatekeeping as in the correct use of a heap in the min max logic for top k stuff

counts = defaultdict(int)
heap = []
for element in nums:
    counts[element] += 1
    datum = (-1 * counts[element], element) # python compares tuples based on index 0 first
    print("datum = {}".format(datum))
    if len(heap) < k:
        print("A")
        heapq.heappush(heap, datum)
    else:
        print("B")
        heapq.heappushpop(heap, datum)
    print("heap = {}".format(heap))
return [datum[1] for datum in heap]
"""

