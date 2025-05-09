class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1): 
            if nums[i] == nums[i + 1]: 
                multi = nums[i] * 2
                nums[i] = multi
                nums[i + 1] = 0
            else: 
                continue
        
        seeker = 0
        holder = 0

        while seeker < len(nums): 
            if nums[seeker] != 0: 
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                seeker+=1
                holder+=1
            else: 
                seeker+=1

        return nums