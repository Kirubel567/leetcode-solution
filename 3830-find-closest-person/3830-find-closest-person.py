class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1, diff2 = abs(x - z), abs(y-z)

        if diff1 == diff2: 
            return 0
        return 1 if diff1 < diff2 else 2