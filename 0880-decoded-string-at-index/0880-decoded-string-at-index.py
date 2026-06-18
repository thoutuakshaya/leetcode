class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        leni=0
        for i in s:
            if i.isalpha():
                leni+=1
            elif i.isdigit():
                leni*=int(i)
        for i in reversed(s):
            k%=leni
            if k==0 and i.isalpha():
                return i
            elif i.isdigit():
                leni//=int(i)
            else:
                leni-=1