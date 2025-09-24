class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0]) #the length of rows and columns

        result = [[0] * COLS for _ in range(ROWS)] #create a grid of ROWS X COLS

        for r in range(ROWS): 
            for c in range(COLS): #iterate through each cells
                total, count = 0, 0
                for i in range(r-1, r+2): # r+2 to include r+1
                    for j in range(c-1, c+2): 
                        if i < 0 or i == ROWS or j == COLS or j < 0: #this is to jump those that are at the edge and near the edge
                            continue
                        total += img[i][j]
                        count += 1

                result[r][c] = total//count
        
        return result
