class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            k=26-(ord(s[i])-ord('a'))
            ans+=(i+1)*k
        return ans