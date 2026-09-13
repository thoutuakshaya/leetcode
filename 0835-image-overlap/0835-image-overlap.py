class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        s1=[]
        s2=[]
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j]==1:
                    s1.append((i,j)) 
        for i in range(len(img2)):
            for j in range(len(img2)):
                if img2[i][j]==1:
                    s2.append((i,j)) 
        k={}
        for i in s1:
            for j in s2:

                x=i[0]-j[0]
                y=i[1]-j[1]
                k[(x,y)]=k.get((x,y),0)+1
        res=0
        for val in k.values():
            res=max(val,res)
        return res
        