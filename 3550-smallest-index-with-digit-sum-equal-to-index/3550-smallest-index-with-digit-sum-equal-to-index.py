class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i , num in enumerate(nums):
            
            s=0
            while num>0:
                s+=num%10
                num=num//10
            if s==i:
                return i
        return -1