class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for i in range(len(words)):
            s=0
            for j in words[i]:
                s+= weights[ord(j)-ord('a')]
            h=s%26
            ans+=chr(ord("z")-h)
        return ans

                

            


        