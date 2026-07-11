from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):

            visited[node] = True

            vertices = 1
            edgeCount = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, e = dfs(nei)
                    vertices += v
                    edgeCount += e

            return vertices, edgeCount

        for i in range(n):

            if not visited[i]:

                vertices, edgeCount = dfs(i)

                edgeCount //= 2

                if edgeCount == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans