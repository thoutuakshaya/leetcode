class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sums=sum(nums)
        ansa=[]
        left=0
        
        ans=0
        for i in range(len(nums)):
            right=sums-left-nums[i]
            ansa.append(abs(right-left))
            left+=nums[i]
        return ansa