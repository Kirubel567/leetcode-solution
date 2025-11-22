class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        holder, seeker = 0, 0

        while seeker < len(nums): 
            if nums[seeker] != val: 
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1
        return holder
