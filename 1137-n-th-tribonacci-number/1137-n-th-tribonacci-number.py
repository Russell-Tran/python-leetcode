class Solution:
    def tribonacci(self, n: int) -> int:
        storage = {
            0 : 0,
            1 : 1,
            2 : 1
        }
        if n in storage:
            return storage[n]
        
        i = 3
        while i <= n:
            storage[i] = storage[i-1] + storage[i-2] + storage[i-3]
            i += 1
        
        return storage[n]