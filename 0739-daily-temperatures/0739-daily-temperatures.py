class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                waiting_idx, _ = stack.pop()
                result[waiting_idx] = i - waiting_idx
            stack.append((i, temperature))
        return result
"""

the last element is always going to be zeroj


[73,74,75,71,69,72,76,73]

[1, 1, 4]

this problem is not as obvious as others.

maybe push the indices that are "owed"?

kind of weird that this is allegedly a stack problem and not a 
min heap problem 

editorial solution: use a monotonic stack



"""