class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        minValue = nums[k-1] - nums[left]

        for r in range(k, len(nums)): 
            left += 1
            minValue = min(minValue, nums[r] - nums[left])
        
        return minValue


