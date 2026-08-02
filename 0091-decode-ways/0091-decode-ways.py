class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            
            # Use the single index
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            # Use the last two indexes
            if i >= 2:
                two_digits = int(s[i-2] + s[i-1])

                if 10 <= two_digits <= 26:
                    dp[i] += dp[i-2]
        
        return dp[-1]