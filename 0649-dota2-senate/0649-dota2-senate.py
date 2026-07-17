from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        d=deque()
        r=deque()
        for i,ch in enumerate(senate):
            if ch=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r1=r.popleft()
            d1=d.popleft()
            if r1<d1:
                r.append(r1+n)
            else:
                d.append(d1+n)
        return "Radiant" if r else "Dire"