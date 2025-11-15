class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        max_profit  = 0

        for right in range(len(prices)):

            profit = prices[right] - prices[left]

            if profit < 0:
                left = right

            max_profit = max(max_profit, profit)
        
        return max_profit
