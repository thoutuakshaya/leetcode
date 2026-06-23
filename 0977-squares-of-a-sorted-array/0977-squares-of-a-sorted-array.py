class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums)):
            k.append(nums[i]*nums[i])
        k.sort()
        return k
