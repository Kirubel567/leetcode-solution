class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)): 
            if nums[i-1] == nums[i]: 
                return nums[i]
    