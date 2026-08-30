class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l=len(nums)
        k=nums[:]
        k.sort()
        mini=nums.index(k[0])
        maxi=nums.index(k[-1])
        first=min(mini,maxi)
        last=max(mini,maxi)
        return min(last+1,l-first,(first+1+(l-last)))