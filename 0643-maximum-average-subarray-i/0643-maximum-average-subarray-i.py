class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        t=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            t=max(t,s)
        return t/k