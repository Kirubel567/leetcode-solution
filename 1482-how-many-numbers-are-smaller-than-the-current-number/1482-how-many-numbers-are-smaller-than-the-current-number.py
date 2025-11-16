class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        compare = sorted(nums)
        mapp = defaultdict(int)
        for i in range(len(compare)): 
            if compare[i] not in mapp: 
                mapp[compare[i]] = i
        
        res = []
        for i in range(len(nums)): 
            res.append(mapp[nums[i]])

        return res 

