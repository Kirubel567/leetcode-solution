class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator =0
        res =[]
        for i in range(len(nums)): 
            accumulator += nums[i]
            res.append(accumulator)
        return res 