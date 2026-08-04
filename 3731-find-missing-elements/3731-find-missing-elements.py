class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        first=nums[0]
        last=nums[-1]
        k=0
        for i in range(first ,last+1):
            k+=i
        total=sum(nums)
        if abs(total-k)==0:
            return []
        else:
            l=[]
            for j in range(first,last+1):
                
                if j not in nums:
                    l.append(j)
            return l
        