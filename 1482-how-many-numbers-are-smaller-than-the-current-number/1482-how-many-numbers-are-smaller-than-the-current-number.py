class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)): 
                if (i != j): 
                    if nums[j] < nums[i]: 
                        count += 1  
            arr.append(count)
            count = 0

        return arr       