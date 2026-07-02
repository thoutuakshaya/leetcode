from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]

        start = grid[0][0]
        dist[0][0] = start

        dq = deque()
        dq.append((0, 0))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while dq:
            x, y = dq.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    cost = grid[nx][ny]
                    new_cost = dist[x][y] + cost

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost

                        if cost == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return health - dist[m - 1][n - 1] >= 1