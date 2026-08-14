class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False]*len(isConnected)
        def connect(city):
            visited[city]=True
            for i in range(len(isConnected)):
                if isConnected[city][i]==1 and not visited[i]:
                    connect(i)
        pr=0
        for ci in range(len(isConnected)):
            if not visited[ci]:
                pr+=1
                connect(ci)
        return pr


            

