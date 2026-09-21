class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with num
            r = num % k
            new_dp[r] += 1

            # Extend previous subarrays
            for old_r in range(k):
                new_r = (old_r * num) % k
                new_dp[new_r] += dp[old_r]

            dp = new_dp

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += dp[r]

        return ans