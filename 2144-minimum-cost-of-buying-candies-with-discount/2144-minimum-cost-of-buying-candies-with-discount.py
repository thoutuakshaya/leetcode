class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        sum1=0
        for i in range(len(cost)):
            if ((i+1)%3!=0):
                sum1+=cost[i]
            
        return sum1