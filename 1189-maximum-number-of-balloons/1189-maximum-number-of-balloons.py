class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=[]
        a=[]
        l=[]
        o=[]
        n=[]
        for st in text:
            if st =="b":
                b.append(st)
            elif st=="a":
                a.append(st)
            elif st=="l":
                l.append(st)
            elif st=="o":
                o.append(st)
            elif st=="n":
                n.append(st)
        
        return  min(len(b),len(a),len(l)//2, len(o)//2, len(n))
