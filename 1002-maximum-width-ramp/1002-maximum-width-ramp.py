class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(i)
        
        max_width = 0
       
        for j in reversed(range(len(nums))): 
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width
