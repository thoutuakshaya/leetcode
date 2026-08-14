class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        k={}
        first=0
        m=0
        for i in range(len(s)) :
            k[s[i]]=k.get(s[i],0)+1
        
            while k[s[i]]>2:
                k[s[first]]-=1
                first+=1
            m=max(m,i-first+1)
        return m