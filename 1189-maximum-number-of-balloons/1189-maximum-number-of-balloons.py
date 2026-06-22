from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        return min( c["a"],c["b"],c["o"]//2,c["l"]//2,c["n"])