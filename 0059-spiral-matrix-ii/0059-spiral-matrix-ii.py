class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n-1
        top, bottom = 0, n-1

        #create a matrix of n*n
        matrix = [[0] * n for _ in range(n)]
        #have a counter to know the current number to add to the matrix 
        counter = 1

        while left <= right and top<=bottom:#or only one of the two condition would work 
            for i in range(left, right+1): 
                matrix[top][i] = counter
                counter += 1
            top += 1

            for i in range(top, bottom+1): 
                matrix[i][right] = counter
                counter+=1
            right -= 1
            
            for i in range(right, left-1, -1): 
                matrix[bottom][i] = counter
                counter+= 1
            bottom-=1

            for i in range(bottom, top-1, -1): 
                matrix[i][left] = counter
                counter+= 1
            left += 1
        
        return matrix