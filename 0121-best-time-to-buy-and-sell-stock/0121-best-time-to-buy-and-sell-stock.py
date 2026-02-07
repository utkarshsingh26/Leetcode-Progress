class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            if profit < 0:
                left = right
        
        return max_profit