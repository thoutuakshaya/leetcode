class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        s=(2*n*(2*n+1))/2
        s1=0
        for i in range(1,n*2+1):
            if i%2 ==0:
                s1+=i
        s2=s-s1
        while s2!=0:
            s1,s2=s2,s1%s2
        return int(abs(s1))
