class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0 
        right = len(height) - 1
        area = 0

        while left < right:
            calculate = min(height[left], height[right]) * (right - left) 
            area = max(area, calculate)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1


        return area
            


        