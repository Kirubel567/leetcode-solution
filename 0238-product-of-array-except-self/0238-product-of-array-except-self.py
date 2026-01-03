class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #store the pref and postfix multiplication first 
        preMult = [1] * (len(nums)+1)
        postMult = [1] * (len(nums)+1)
        prod = 1
        for i in range(len(nums)-1, -1, -1): 
            prod *= nums[i]
            postMult[i] *= prod
        prod = 1
        for i in range(len(nums)): 
            prod *= nums[i]
            preMult[i+1] *= prod
        
        print(preMult)
        print(postMult)
        res = [0] * len(nums)
        for i in range(len(nums)): 
            res[i] = preMult[i] * postMult[i+1]
        return res 
            

