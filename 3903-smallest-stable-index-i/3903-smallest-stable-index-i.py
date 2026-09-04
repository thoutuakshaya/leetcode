class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if n==1 or len(set(nums))==1:
            return 0
        minimum=[nums[-1]]*n
        for i in range(n-2,-1,-1):
            minimum[i]=min(nums[i],minimum[i+1])
        maximum=[nums[0]]*n
        for j in range(1,n):
            maximum[j]=max(nums[j],maximum[j-1])
        for ki in range(n):
            l=maximum[ki]-minimum[ki]
            if l<=k:
                return ki
        return -1
