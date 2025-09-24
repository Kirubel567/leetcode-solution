class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1): 
            if nums[i] == nums[i+1]: 
                nums[i] = nums[i] *2
                nums[i +1] = 0
        
        #now use two pointers holder and seeker to group zeros to the end 
        holder, seeker = 0, 0
        while seeker< len(nums): 
            if nums[seeker] != 0: 
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1

        return nums