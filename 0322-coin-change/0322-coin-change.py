class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    remaining_amount = current_amount - coin

                    dp[current_amount] = min(dp[current_amount], dp[remaining_amount] + 1)
        
        for i in range(len(dp)):
            if dp[i] == float("inf"):
                dp[i] = -1
        
        return dp[-1]