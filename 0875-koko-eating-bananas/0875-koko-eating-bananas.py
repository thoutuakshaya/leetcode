class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini=1
        maxi=max(piles)
        while mini<maxi:
            hours=0
            mid=mini+(maxi-mini)//2
            for i in piles:
                hours+=(i+mid-1)//mid
            if hours<=h:
               maxi=mid
            else:
                mini=mid+1
        return mini
                    

# Why -1?
# The general trick is:
# (a + b - 1) // b
# means ceil(a / b).