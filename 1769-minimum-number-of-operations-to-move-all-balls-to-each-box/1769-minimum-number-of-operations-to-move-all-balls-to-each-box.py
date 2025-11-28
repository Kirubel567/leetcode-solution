class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #when iterating through the array we are moving balls only one place as a time, but at a time we could move more than one balls so moves = 1, and numBall, then the total number of movement would be moves * numBall, but moves is 1 at a time so it would be numBall of movement at a time

        #left portion each element 
        moves, balls = 0, 0
        res = [0]*len(boxes)
        for i in range(len(boxes)): 
            moves = moves + balls
            res[i] = moves
            
            if boxes[i] == "1": 
                balls +=1 

        #right portion of each element 
        moves, balls = 0, 0
        for i in range(len(boxes)-1, -1, -1):
            moves = moves + balls
            res[i] += moves
            
            if boxes[i] == "1": 
                balls +=1 
        
        return res 

