class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""

        for word in words:
            s = 0

            for ch in word:
                s += weights[ord(ch) - ord('a')]

            rem = s % 26
            ans += chr(ord('z') - rem)

        return ans
                

            


        