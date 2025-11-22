class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 2: 
            return res
        if numRows == 1: 
            return [[1]]
        for i in range(2, numRows): 
            curr = [1]*(i+1)
            for j in range(1, len(curr)-1): 
                curr[j] = res[i-1][j-1] + res[i-1][j]
            res.append(curr)
        return res 
            
            
                