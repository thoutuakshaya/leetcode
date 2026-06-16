class Solution:
    def processStr(self, s: str) -> str:
        
        q=[]
        for i in s:
            if i not in "*#%":
                q.append(i)
            elif (i=="*"):
                if q:
                    q.pop()
            elif (i=="#"):
                q.extend(q)
            elif (i=="%"):
                q=q[::-1]
            else:
                return
        return "".join(q)
