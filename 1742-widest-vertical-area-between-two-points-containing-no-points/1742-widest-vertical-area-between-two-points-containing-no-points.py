class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = []
        for i in range(len(points)): 
            for j in range(1): 
                res.append(points[i][j])

        res.sort()
        Max = -float('inf')
        for i in range(len(res)-1): 
            Max = max(Max, res[i+1] - res[i])

        return Max