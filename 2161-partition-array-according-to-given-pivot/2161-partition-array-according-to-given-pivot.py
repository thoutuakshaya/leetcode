class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        left=[]
        right=[]
        Pi=[]
        for i in range(n):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])
            elif nums[i]==pivot:
                Pi.append(nums[i])
        return left+Pi+right