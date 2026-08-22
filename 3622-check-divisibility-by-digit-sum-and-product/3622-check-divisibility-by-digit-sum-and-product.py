class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        m=1
        for i in str(n):
            s+=int(i)
            m*=int(i)
        k=s+m
        if n%k ==0:
            return True
        else:
            return False