class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #negetive, negetice prev positive , positive prev positive,postive pre negetive, negetive pre negetive
        arr=[]
        for i in asteroids:
            if i>0:
                arr.append(i)
            else:
                
                while arr and arr[-1]>0 and abs(i)>arr[-1]:
                    arr.pop()
                if not arr or arr[-1]<0 :
                    arr.append(i)
                elif arr[-1]>0 and abs(i)==arr[-1]:
                    arr.pop()
        return arr