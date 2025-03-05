class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0 
        total = 0
        anchor = prices[-1]
        for i in reversed(range(0, len(prices))):
            curr_val = prices[i]
            next_val = prices[i-1]
            if next_val > curr_val or i == 0:
                total += anchor - curr_val
                anchor = next_val
            else:
                pass 

        return total
