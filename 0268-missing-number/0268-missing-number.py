class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #first sort the array
        #iterate through the array and check if the value ain't equal to i
        nums.sort()
        for i in range(len(nums)): 
            if i != nums[i]: 
                return i

        return nums[-1]+1