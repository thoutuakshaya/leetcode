class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        ds=[[0]*(n+1) for _ in range(m+1)]
        for j in range(n + 1):
            ds[0][j] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[j-1]==t[i-1]:
                    ds[i][j]=ds[i-1][j-1]+ds[i][j-1]
                else:
                    ds[i][j]=ds[i][j-1]
        return ds[m][n]