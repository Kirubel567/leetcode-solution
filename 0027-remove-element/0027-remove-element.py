class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        holder, seeker = 0,0

        while seeker < len(nums): 
            if nums[seeker] != val: 
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
            seeker += 1
    
        return holder 

