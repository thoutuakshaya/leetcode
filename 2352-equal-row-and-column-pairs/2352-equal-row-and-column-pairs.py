from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d=defaultdict(int)
        for row in grid:
            d[tuple(row)]+=1
        #here all row comes as first element in list
        n=len(grid)
        ans=0
        for i in range(n):
            k=[]
            for j in range(n):
                k.append(grid[j][i])
            ans+=d[tuple(k)]
        return ans
