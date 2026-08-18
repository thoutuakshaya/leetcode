class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count=[0]*51
        for i in range(len(nums)-k+1):
            window=set(nums[i:i+k])
            
            for x in window:
                count[x]+=1
        for j in range(50 ,-1,-1):
            if count[j]==1:
                return j
        return -1