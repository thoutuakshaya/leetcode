import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap=[]
        ans=0
        sun=0
        ret=0
        pairs=sorted(zip(nums2,nums1),reverse=True)
        for i,j in pairs:
            heapq.heappush(heap,j)
            sun+=j
            if len(heap)>k:
                rem=heapq.heappop(heap)
                sun-=rem
            if len(heap)==k:
                ans=sun*i
                ret=max(ans,ret)
        return ret
                