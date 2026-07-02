class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # k={}
        # for i in nums1 and nums2:
        #     k[i]=1
        # arr=[]
        # for i not in k and in nums1:
        #     arr.append([i)

        nums1=set(nums1)
        nums2=set(nums2)
        return[ list(nums1-nums2),list(nums2-nums1)]