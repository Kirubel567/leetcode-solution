class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rcounter, wcounter, bcounter = 0, 0, 0
        for i in range(len(nums)): 
            if nums[i] == 0: 
                rcounter += 1
            elif nums[i] == 1: 
                wcounter += 1
            else: 
                bcounter += 1

        for i in range(len(nums)): 
            if rcounter >0: 
                nums[i] = 0
                rcounter-=1
            elif wcounter >0: 
                nums[i] = 1
                wcounter -=1
            else: 
                nums[i] = 2
                
            
        