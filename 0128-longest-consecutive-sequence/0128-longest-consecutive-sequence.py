class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ans = -float('inf') 
        counter = 0
        nums = sorted(set(nums))
        if not nums: 
            return 0
        elif len(nums) == 1: 
            return 1
        for i in range(len(nums) - 1): 
            if nums[i] + 1 == nums[i+1]: 
                counter += 1
            else: 
                counter = 0

            ans = max(counter, ans)

        return ans + 1