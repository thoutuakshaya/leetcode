class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        count=0
        costs.sort()
        for i in range(len(costs)):
            if  costs[i]>coins:
                break
            coins-=costs[i]
            count+=1    
            
        return count

        