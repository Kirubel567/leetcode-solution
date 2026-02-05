class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = {i for i in range(left, right+1)}
        print(check)
        Set = set()
        for j in range(len(ranges)): 
            Set.update(range(ranges[j][0], ranges[j][1]+1))

        return check <= Set