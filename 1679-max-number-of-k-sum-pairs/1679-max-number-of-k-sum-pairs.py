from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # greedy approach
        # you can prove by induction that any pair you pick out, there couldn't be a better world
        # since two numbers sum to k , those two numbers are always partners
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        
        exception = None
        if k % 2 == 0:
            exception = k // 2
        
        total = 0
        seen = set()
        for num, count in counts.items():
            if num not in seen:
                if exception is not None and num == exception:
                    total += count // 2
                else:
                    other_num = k - num
                    if other_num in counts:
                        total += min(count, counts[k-num])
                    seen.add(num)
                    seen.add(other_num)
        
        return total
            
        
        