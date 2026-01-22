# https://www.geeksforgeeks.org/dsa/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:

    def _reference_max_profit(prices: List[int]) -> int:
    
        min_price = float("inf")
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            best = max(best, p - min_price)
        return best