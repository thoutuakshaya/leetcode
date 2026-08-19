class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))
        visited=[False]*n
        def dfs(node):
            visited[node]=True
            change=0
            for neighbour , direction in graph[node]:
                if not visited[neighbour]:
                    change+=direction
                    change+=dfs(neighbour)
            return change
        return dfs(0)