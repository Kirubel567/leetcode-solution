class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = {0:1}
        Sum, res = 0, 0

        for i in range(len(nums)): 
            Sum += nums[i]
            diff = Sum - k


            if diff in mapp: 
                res += mapp[diff] #add the frequency to the result 
                
            mapp[Sum] = mapp.get(Sum, 0) + 1 #add the frequency of the sum to the dictionary
        
        return res 