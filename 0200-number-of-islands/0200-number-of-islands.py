class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        directions={
                (0,1),
                (1,0),
                (0,-1),
                (-1,0)
            }
        count=0
        def dfs(i,j):
            

            grid[i][j]='0'
            for nr,nc in directions:
                newr=nr+i
                newc=nc+j
                if (0<=newr<=n-1 and 0<=newc<=m-1 and grid[newr][newc]=='1'):
                        dfs(newr,newc)
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count
                        
                
