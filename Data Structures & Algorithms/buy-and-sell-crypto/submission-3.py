class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dict_x = {}
        biggest = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]>prices[j]:
                    continue
                else:
                    if prices[j]-prices[i]>biggest:
                        biggest = prices[j]-prices[i]

            dict_x[i]= biggest

        biggest_value = 0

        for value in dict_x.values():
            if value > biggest_value:
                biggest_value = value

        return biggest_value