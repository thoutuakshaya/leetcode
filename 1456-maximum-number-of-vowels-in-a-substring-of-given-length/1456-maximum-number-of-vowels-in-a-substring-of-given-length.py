class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a","e","i","o","u"}
        count=0
        for i in range(k):
            if s[i] in vowels:
                count+=1
        ans= count
        for j in range(k ,len(s)):
            if s[j] in vowels:
                count+=1
            if s[j-k] in vowels:
                count-=1
            ans=max(count,ans)
        return ans