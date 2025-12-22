class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, next_pos = len(nums)-2, len(nums)-1

        while i >= 0: 
            if i + nums[i] >= next_pos: 
                next_pos =i 
            i-=1
        return True if next_pos == 0 else False