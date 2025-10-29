class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # Step 1: build a decreasing stack of indices
        for i, val in enumerate(nums):
            if not stack or nums[stack[-1]] > val:
                stack.append(i)
        
        max_width = 0
        # Step 2: go from right to left and pop when ramp condition satisfied
        for j in reversed(range(len(nums))):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width
