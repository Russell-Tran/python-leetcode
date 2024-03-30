class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        best = max(candies)
        return [candies[i] + extraCandies >= best for i in range(len(candies))]