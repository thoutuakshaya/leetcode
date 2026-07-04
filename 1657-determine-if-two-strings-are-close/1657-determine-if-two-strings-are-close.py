class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        k={}
        h={}
        for i in word1:
            k[i]=k.get(i,0)+1
        for j in word2:
            h[j]=h.get(j,0)+1
        if set(h.keys())!=set(k.keys()):
            return False
        if sorted(k.values())!=sorted(h.values()):
            return False
    
        return True
             