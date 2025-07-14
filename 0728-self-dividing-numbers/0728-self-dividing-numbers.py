class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        count = 0
        vect = []
        for i in range(left, right + 1): 
            check = True
            m = i 
            while m > 0: 
                digit = m % 10
                if digit == 0 or i % digit != 0: 
                    check = False 
                    break   
                m = m // 10
            if check == True: 
                vect += [i]
        
        return vect
            
                