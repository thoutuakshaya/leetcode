class Solution:
    def rob(self, nums: list[int]) -> int:
        dp=[0]*(len(nums)+1)
        dp[1]=nums[0]
        dp[2]=nums[1]
        for i in range(3,len(nums)+2):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[len(nums)+1]