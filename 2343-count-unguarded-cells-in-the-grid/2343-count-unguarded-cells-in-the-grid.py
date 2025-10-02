class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        #guard = 1, unguarded = 0, guarded = 3, wall = 4
        for r, c in guards: 
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 4

        
        def mark_guard(r, c): #to iterate through the matrix and mark the guarded 
            for row in range(r+ 1, m): 
                if grid[row][c]  in [1, 4]: 
                    break
                
                grid[row][c] = 3
            
            for row in reversed(range(0, r)): 
                if grid[row][c]  in [1, 4]: 
                    break
                
                grid[row][c] = 3
            
            for col in range(c+ 1, n): 
                if grid[r][col] in [1, 4]: 
                    break
                
                grid[r][col] = 3
            
            for col in reversed(range(0, c)): 
                if grid[r][col] in [1, 4]: 
                    break
                
                grid[r][col] = 3


        for r, c in guards: 
            mark_guard(r, c)#using the guards we mark the guarded cells
        
        res =0
        for row in grid: 
            for n in row: 
                if n == 0: 
                    res += 1
        
        return res 




