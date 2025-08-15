class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        res = [0] * len(nums)
        accumulator = 1
        mapp = Counter(nums)

        #check if there is more than one 0
        if mapp[0] > 1: 
            return res

        #create the prefix 
        for i in range(len(nums)): 
            if(nums[i] == 0):
                continue
            accumulator *= nums[i]
            prefix.append(accumulator)
        

        #if a zero is found just return the product on that index
        for i in range(len(nums)): 
            if nums[i] == 0: 
                res[i] = prefix[len(prefix) - 1]
                return res

        for i in range(len(prefix)): 
            res[i] = prefix[len(prefix) - 1]//nums[i]
        return res 
