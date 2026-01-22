class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        counter = 0
        while any(nums[i] > nums[i+1] for i in range(len(nums)-1)):
            
            min_sum = nums[0] + nums[1]
            index = 0
            for i in range(1, len(nums)-1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    index = i
        
            nums[index] = min_sum
            nums.pop(index+1)
            counter += 1
        return counter