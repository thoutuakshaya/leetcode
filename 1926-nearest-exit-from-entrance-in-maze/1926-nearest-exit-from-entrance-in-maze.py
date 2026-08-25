from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n=len(maze)
        m=len(maze[0])
        queue=deque([entrance])
        #creating que and adding entrance node to it
        maze[entrance[0]][entrance[1]]='+'
        directions=[
            (-1,0),
            (1,0),
            (0,1),
            (0,-1)
        ]
        steps=0

        while queue:
            for _ in range(len(queue)):
                row, col=queue.popleft()
                for dr ,dc in directions :
                    new_r=row+dr
                    new_c=col+dc
                    if( 0<=new_r <n and
                        0<=new_c<m and
                        maze[new_r][new_c]=='.'):
                        if (new_r==n-1 or
                        new_r==0 or
                        new_c==0 or
                        new_c==m-1):
                            return steps+1
                        maze[new_r][new_c]='+'
                        queue.append((new_r,new_c))
                    
            steps+=1

        return -1     