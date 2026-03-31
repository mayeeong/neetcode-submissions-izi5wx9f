class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = (10**5) + 1
        maximum = 0
        for price in prices:
            if price < minimum:
                minimum = price
            else:
                gap = price - minimum
                maximum = max (gap, maximum)
        return maximum