class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] != nums[left]: 
                left += 1
                nums[left] = nums[right]
            right+=1
        return left + 1
            

           