import random
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        choice = random.choice([1, 2])
        if choice == 1:
            return self._soln1(s, t)
        else:
            return self._soln2(s, t)

    def _soln1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def _soln2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1
        
        return all([count == 0 for count in counts.values()])