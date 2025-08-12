class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()

        for i in range(len(nums) - 2): 
            #check for dublicates of i 
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            
            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right: 
                if nums[left] + nums[right] == target: 
                    arr.append([nums[i], nums[left], nums[right]])

                    #check for duplicates of left 
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1 

                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target: 
                    left += 1
                else: 
                    right -= 1

        return arr  
