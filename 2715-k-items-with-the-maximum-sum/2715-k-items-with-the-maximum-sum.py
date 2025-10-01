class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        #the function = maximum possile sum of numbers written on the items
        #the variable = variables 1, 0, -1
        #the constraint = k

        #start choosing from ones then to numZeroes then finally to numnegs

        Sum, count = 0, 0
        while count < k: 
            if numOnes > 0: 
                Sum += 1
                numOnes -= 1
            elif numZeros > 0: 
                numZeros -= 1
            else: 
                Sum -= 1
                numNegOnes -= 1

            count += 1
        
        return Sum 