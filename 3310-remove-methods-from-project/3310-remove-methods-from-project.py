from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        # Build graph
        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        # Step 1: Find all suspicious methods
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)

            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        # Step 2: Check if any outside node calls a suspicious node
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Step 3: Return remaining methods
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans