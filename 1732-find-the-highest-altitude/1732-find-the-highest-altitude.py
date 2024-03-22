class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        best = 0
        curr = 0
        for delta in gain:
            curr += delta
            best = max(best, curr)
        return best