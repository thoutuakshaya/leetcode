from collections import deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7

        n = len(edges) + 1

        # Build graph
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to find maximum depth
        q = deque([(1, 0)])  # (node, depth)
        visited = [False] * (n + 1)
        visited[1] = True

        maxDepth = 0

        while q:
            node, depth = q.popleft()
            maxDepth = max(maxDepth, depth)

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append((nei, depth + 1))

        # Number of odd-cost assignments
        return pow(2, maxDepth - 1, MOD)