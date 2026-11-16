class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        last=s
        while len(last)>k:
            final=""
            sumi=0
            l=0
            for i in range(len(last)):
                l+=1 
                sumi+=int(last[i])
                if l==k or i ==len(last)-1:
                    final+=str(sumi)
                    sumi=0
                    l=0
            last=final
        return last
                




        