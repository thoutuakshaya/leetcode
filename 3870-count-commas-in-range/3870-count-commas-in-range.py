class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        if n<1000:
            return 0
        if n>=1000:
            count+=n-1000+1
        if n>=1000000:
            count+=n-1000000+1
        return count
        
