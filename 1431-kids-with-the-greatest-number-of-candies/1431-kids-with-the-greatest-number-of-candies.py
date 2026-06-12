class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ar=[]
        
        for i in range(len(candies)):
            booli=True
            for j in range(len(candies)):
                if (candies[i]+extraCandies)< candies[j] :
                    booli=False
                    break
            
            ar.append(booli)
        return ar
