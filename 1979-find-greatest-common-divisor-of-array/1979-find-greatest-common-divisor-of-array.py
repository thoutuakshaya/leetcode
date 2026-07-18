class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        i=nums[0]
        j=nums[-1]
        while i:
            j,i=i,j%i
        return j