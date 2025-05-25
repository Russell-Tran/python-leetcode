class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        lowest_so_far = prices[0]
        best_profit = 0
        for price in prices:
            best_profit = max(best_profit, price - lowest_so_far)
            lowest_so_far = min(lowest_so_far, price)
        return best_profit


"""
prices = [7,1,5,3,6,4]
best = 0  4 
current = 0.  4 . 0 . 3

[7,1,5,3,6,4]
         ^
JUNK - WRONG
profit = 0
for i, price in enumerate(prices[1:], start=1):
    profit += price - prices[i-1] if price > prices[i-1] else 0
    print(profit)
return profit


JUNK - WRONG 2
if len(prices) == 1:
    return 0
best_profit = 0
current_profit = max(0, prices[1] - prices[0])
for i, price in enumerate(prices[2:], start=2):
    if price >= prices[i-1]: # monotonically increasing
        current_profit += price - prices[i-1]
    else:
        best_profit = max(best_profit, current_profit)
        current_profit = 0
best_profit = max(best_profit, current_profit)
return best_profit
"""