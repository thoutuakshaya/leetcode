class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        #return min(nums1)&1 or all(i&1 for i in nums1)
        return min(nums1) % 2 == 1 or all(a % 2 == 0 for a in nums1)