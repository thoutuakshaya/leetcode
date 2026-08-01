from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]

            pickLeft = nums[i] - dp(i + 1, j)
            pickRight = nums[j] - dp(i, j - 1)

            return max(pickLeft, pickRight)

        return dp(0, len(nums) - 1) >= 0