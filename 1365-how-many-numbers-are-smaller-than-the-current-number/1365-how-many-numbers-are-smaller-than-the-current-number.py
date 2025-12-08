class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #[1,2,2,3,8]
        mapp = defaultdict(int)
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)): 
            if sorted_nums[i] not in mapp: 
                mapp[sorted_nums[i]] = i
        
        res = []
        for i in range(len(nums)): 
           res.append(mapp[nums[i]])
        return res 

