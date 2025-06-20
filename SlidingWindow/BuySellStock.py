from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        index = 0
        prices_len = len(prices)
        while prices_len > index:
            if prices[index + 1] > prices[index]:
                for i in range(index, prices_len):
                    new_profit = prices[i] - prices[index]
                    if new_profit > profit:
                        profit = new_profit
                return profit
            else:
                index =+ 1
        
        return profit


sol  = Solution()
print(sol.maxProfit([7,6,4,3,1]))
                