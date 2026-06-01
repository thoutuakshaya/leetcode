class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        r=[0]*n
        s=[]
        prevt=0
        for log in logs:
            f,nme,t=log.split(":")
            f=int(f)
            t=int(t)
            if nme=="start":
                if len(s)>0:
                    r[s[-1]]+=t-prevt
                s.append(f)
                prevt=t
            else:
                r[s.pop()]+=t-prevt+1
                prevt=t+1
        return r