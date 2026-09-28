class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)

        # dp[i][w] = minimum cost to paint w walls
        # using the first i painters
        dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        # 0 walls need 0 cost
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for w in range(1, n + 1):

                # Don't choose this paid painter
                not_pick = dp[i - 1][w]

                # Choose this paid painter
                # He paints 1 wall himself and free painter
                # can paint time[i-1] walls during that time
                covered = 1 + time[i - 1]

                remaining = max(0, w - covered)

                pick = cost[i - 1] + dp[i - 1][remaining]

                dp[i][w] = min(pick, not_pick)

        return dp[n][n]