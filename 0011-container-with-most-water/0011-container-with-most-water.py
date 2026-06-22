class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        left=0
        ans=0
        while left<right:
            widht=abs(left-right)
            area=widht*(min(height[right],height[left]))
            ans=max(area,ans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
        