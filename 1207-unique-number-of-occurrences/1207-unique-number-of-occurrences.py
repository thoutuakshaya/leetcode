class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        k={}
        for i in arr :
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        
        if len(set(k.values()))==len(k.values()):
            return True
        else:
            return False
