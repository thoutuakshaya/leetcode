class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        k=n
        while k>=n:
            l=1
            for i in str(k):
                l*=int(i)
            if l%t ==0:
                return k
            k=k+1
        return 
