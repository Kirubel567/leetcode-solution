class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left, right, count = 0, len(nums)-1, 0
        nums.sort()
        while left < right: 
            if nums[right]+nums[left] > k: 
                right -=1
            elif nums[right]+nums[left]<k:
                left += 1
            else: 
                count += 1
                left += 1
                right -=1
        
        return count