class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        k=sum(stones)
        best=k
        for i in range(len(stones)-2,0,-1):
            k-=stones[i+1]
            best=max(best,k-best)
        return best