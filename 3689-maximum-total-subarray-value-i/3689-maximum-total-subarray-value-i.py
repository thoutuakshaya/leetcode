class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m=max(nums)
        M=min(nums)
        
        result=m-M
        return k*result