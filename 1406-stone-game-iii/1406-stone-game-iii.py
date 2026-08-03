from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0

            best = float("-inf")
            take = 0

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                best = max(best, take - dp(j + 1))

            return best

        diff = dp(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"