from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def dp(i):
            if i>=len(stoneValue):
                return 0
            best=float("-inf")
            take=0
            for j in range(i,min(i+3,len(stoneValue))):
                take+=stoneValue[j]
                best=max(best,take-dp(j+1))
            return best
        diff=dp(0)
        if diff<0:
            return "Bob"
        elif diff>0:
            return "Alice"
        else:
            return "Tie"