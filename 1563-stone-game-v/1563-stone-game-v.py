class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # dp[i][j] = answer for subarray i...j
        dp = [[0] * n for _ in range(n)]

        # mx[i][j] is a helper:
        # max(sum(i...k) + dp[i][k]) for k in [i, j]
        #
        # We also use mx[j][i] in the reverse direction.
        mx = [[0] * n for _ in range(n)]

        # Base case: one stone
        for i in range(n):
            mx[i][i] = stoneValue[i]

        for j in range(1, n):

            # mid = boundary between left and right
            mid = j

            # sum of current interval [i...j]
            sm = stoneValue[j]

            # sum of the right part
            right = 0

            # Move i from right to left
            for i in range(j - 1, -1, -1):

                sm += stoneValue[i]

                # Move mid left while:
                #
                # 2 * right_sum <= total_sum
                #
                # This finds the point where the two
                # partition sums cross.
                while (right + stoneValue[mid]) * 2 <= sm:
                    right += stoneValue[mid]
                    mid -= 1

                # Equal sums
                if right * 2 == sm:
                    dp[i][j] = mx[i][mid]

                # left sum < right sum
                if mid != i:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[i][mid - 1]
                    )

                # right sum < left sum
                if mid != j:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[j][mid + 1]
                    )

                # Update helper for left side
                mx[i][j] = max(
                    mx[i][j - 1],
                    dp[i][j] + sm
                )

                # Update helper for right side
                mx[j][i] = max(
                    mx[j][i + 1],
                    dp[i][j] + sm
                )

        return dp[0][n - 1]