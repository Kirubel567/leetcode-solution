class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1): 
            if nums[i] == nums[i+1]: 
                nums[i+1] = 0
                nums[i] *= 2
        print(nums)
        

        seeker, holder = 0, 0
        while seeker < len(nums): 
            if nums[seeker] != 0: 
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
            seeker += 1
        
        return nums