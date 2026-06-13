class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=[]
        vo=[]
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                arr.append(i)
                vo.append(s[i])
        vo.reverse()
        s=list(s)
        for j in range(len(arr)):
            s[arr[j]]=vo[j]
        return "".join(s)

        