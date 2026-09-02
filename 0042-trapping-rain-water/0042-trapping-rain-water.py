class Solution:
    def trap(self, height: List[int]) -> int:
        left=s=0
        right=len(height)-1
        r_max,l_max=0,0
        while left<right:
            if height[left]<=height[right]:
                if height[left]>l_max:
                    l_max=height[left]
                else:
                    s+=l_max-height[left]

                left+=1
            else:
                if height[right]>r_max:
                    r_max=height[right]
                else:
                    s+=r_max-height[right]
                right-=1
        return s