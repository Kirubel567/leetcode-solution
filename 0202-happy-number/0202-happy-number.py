class Solution:
    def isHappy(self, n: int) -> bool:
        #detect some type of a loop if loop then return false 
        #add the sum of the square into a hashmap and if the sum of the square is repeated ever again return false ez
        #the main problem is getting each digit from the number

        #put the sum as a key and the value anything for now 
        mapp = {}
        
        while n != 1: 
            Sum = 0
            for num in str(n): 
                Sum += int(num) ** 2

            n = Sum 
            if Sum in mapp: 
                return False

            mapp[Sum] = True 
        
        return True 
        
        