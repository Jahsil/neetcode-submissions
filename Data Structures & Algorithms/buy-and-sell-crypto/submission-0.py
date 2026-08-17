class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maxProfit = 0 

        left = 0 

        for right in range(1, N):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
                continue
            else:
                maxProfit = max(maxProfit, profit)
        return maxProfit

            
