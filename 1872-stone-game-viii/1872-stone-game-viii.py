class Solution:
    def stoneGameVIII(self, stones):
        # Calculate total prefix sum
        total = sum(stones)

        # Initially, Alice can take all stones
        best = total

        # Move backwards
        for i in range(len(stones) - 2, 0, -1):
            total -= stones[i + 1]
            best = max(best, total - best)

        return best