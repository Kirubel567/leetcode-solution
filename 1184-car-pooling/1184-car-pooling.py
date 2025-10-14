class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0]*1001 #this is based on the given constraint the kilometer doesnt exceed 1000

        for numPass, start, end in trips: 
            passChange[start] += numPass #add the number of passengers in the begining 
            passChange[end] -= numPass #subtract the number of passengers when the leave

        currPass = 0
        for passengers in passChange: 
            currPass += passengers #after accumulation of changes in passChange, calculate the current passengers present 
            if currPass > capacity: 
                return False
        return True