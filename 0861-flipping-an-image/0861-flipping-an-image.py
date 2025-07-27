class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        horizontalReverse = []
        for row in range(len(image)): 
            horizontalReverse.append(image[row][::-1])
        
        for i in range(len(horizontalReverse)): 
            for j in range(len(horizontalReverse[i])): 
                if horizontalReverse[i][j] == 0: 
                    horizontalReverse[i][j] = 1
                else: 
                    horizontalReverse[i][j] = 0
        
        return horizontalReverse