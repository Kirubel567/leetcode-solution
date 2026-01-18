class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rowSum = [[0]*(n+1) for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                rowSum[i][j+1] = rowSum[i][j] + grid[i][j]

        colSum = [[0] * n for _ in range(m+1)]
        for j in range(n): 
            for i in range(m): 
                colSum[i+1][j] = colSum[i][j] + grid[i][j]
        
        for edge in range(min(m, n), 1, -1): 
            for i in range(m - edge+1): 
                for j in range(n - edge +1): 
                    d1 = sum(grid[i+k][j+k] for k in range(edge))
                    d2 = sum(grid[i + k][j + edge - 1 -k] for k in range(edge))
                    if d1!=d2: continue

                    is_magic = True
                    for k in range(edge): 
                        r_sum = rowSum[i+k][j+edge] - rowSum[i+k][j]
                        c_sum = colSum[i+edge][j+k] - colSum[i][j+k]
                        if r_sum != d1 or c_sum != d1: 
                            is_magic = False
                            break 
                    
                    if is_magic: 
                        return edge
        return 1