class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        #this question has relation with the product of array except self 
        #you can try to do this question the naive way by finding the sum and subtracting n*nums[i] from the sum, but this only works for the starting and ending elements, the array is sorted so, we need to subtract the post_sum - nums[i]* n for the greater elements and nums[i]* n - pref_sum then add the two, instead of decrementing from the whole sum do it in parts(almost the same thing but this works)
        pref_sum, post_sum = 0, 0
        pref = [0]*len(nums)
        post=[0]*len(nums)

        for i in range(len(nums)): 
            pref[i] = pref_sum
            pref_sum += nums[i]
           

        for i in range(len(nums) -1, -1, -1):
            post[i] = post_sum 
            post_sum += nums[i]
            
        res = [0]*len(nums)
        for i in range(len(nums)): 
            res[i] += (i*nums[i]) - pref[i]
            res[i] += post[i] - (len(nums)-i-1)*nums[i]
        
        return res 

