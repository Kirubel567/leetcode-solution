class Solution:
    def minElement(self, nums: List[int]) -> int:
        SumList = [] #The final list I want to put the sum of the digits of the elements
        for i in nums: #accessing each elements of the list, to add the lists
            Elements = list(str(i)) #chaning eacch elements to list to add the digits
            SumOfDigits = 0 
            for j in Elements: #accessing each digits in each element
                SumOfDigits += int(j) #adding the digits
            SumList += [SumOfDigits] #concatinating each sum to create a list of sum of each elements

        return min(SumList)

        

        