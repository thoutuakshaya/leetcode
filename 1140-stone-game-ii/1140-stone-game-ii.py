class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # starting from pile i with M
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(n, 0, -1):

                # Can take all remaining piles
                if i + 2 * M >= n:
                    dp[i][M] = suffix[i]
                    continue

                best = 0

                for X in range(1, 2 * M + 1):
                    next_i = i + X
                    next_M = max(M, X)

                    current = suffix[i] - dp[next_i][next_M]

                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]