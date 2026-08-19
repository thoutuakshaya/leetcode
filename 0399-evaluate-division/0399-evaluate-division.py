class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        for i in range(len(equations)):
            a,b=equations[i]
            value=values[i]
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append((b,value))
            graph[b].append((a,1/value))
        def dfs(cur,tar,visited):
            if cur==tar:
                return 1
            visited.add(cur)
            for neighbour,weight in graph[cur]:
                if neighbour in visited:
                    continue
                result=dfs(neighbour,tar,visited)
                if result!=-1:
                    return result*weight
            return -1

        
        answer=[]
        for a,b in queries:
            if a not in graph or b not in graph:
                answer.append(-1.0)
                continue
            answer.append(dfs(a,b,set()))
        return answer

                