class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        for spell in spells:
            left=0
            right=len(potions)
            while left<right:
                mid=left+(right-left)//2
                if spell*potions[mid] >=success:
                    right=mid
                else:
                    left=mid+1
            ans.append(len(potions)-left)
        return ans
                
