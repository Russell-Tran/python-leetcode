class Solution:
    def recurse(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in self.seen:
            return self.seen[n]
        
        num_paths = self.recurse(n-1) + self.recurse(n-2)
        self.seen[n] = num_paths
        return num_paths
    
    def climbStairs(self, n: int) -> int:
        self.seen = {}
        return self.recurse(n)