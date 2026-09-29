class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return ( nums[0]-1)*(nums[1]-1)