class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:

                left=(flowerbed[i-1]==0 or i==0)
                right= (len(flowerbed)-1==i or flowerbed[i+1]==0)

                if left and right:
                    flowerbed[i]=1
                    c+=1
        return c>=n

        