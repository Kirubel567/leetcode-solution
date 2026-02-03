class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        increasing, count = True, 1
        if nums[1] <= nums[0]: 
            return False
        for i in range(1, len(nums)): 
            if increasing and nums[i] < nums[i-1]: 
                count += 1
                increasing = False
            elif not increasing and nums[i] > nums[i-1]: 
                count += 1
                increasing = True
            
            if nums[i] == nums[i-1]: 
                return False
        print(count)
        return count == 3

            
            


