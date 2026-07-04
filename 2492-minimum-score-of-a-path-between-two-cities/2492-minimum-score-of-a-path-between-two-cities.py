from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        q = deque([1])
        visited = {1}
        ans = float("inf")

        while q:
            node = q.popleft()

            for nei, dist in graph[node]:
                ans = min(ans, dist)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans