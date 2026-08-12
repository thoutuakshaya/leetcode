class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        #frequency dict
        #sliding window
        first=0
        m=0
        ki={}
        for i in range(first,len(nums)):
            
            ki[nums[i]]=ki.get(nums[i],0)+1
            while ki[nums[i]]>k:
                ki[nums[first]]-=1
                first+=1
            m=max(m,i-first+1)
        return m
                