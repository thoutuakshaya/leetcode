class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        INF= float('inf')
        dp=[INF]*(amount+1)
        dp[0]=0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin and dp[i-coin]+1< dp[i]:
                    dp[i]=dp[i-coin]+1
        return dp[amount] if dp[amount]<INF else -1