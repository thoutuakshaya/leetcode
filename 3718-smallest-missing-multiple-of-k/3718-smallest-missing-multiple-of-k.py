class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans,n=1,1
        found=True
        for i in (nums):
            
            while found:
                if k*n in nums:
                    n+=1
                else:
                    found=False
                    ans=k*n
        return ans
