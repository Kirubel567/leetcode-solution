class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = dict()

        for i in range(len(nums)): 
            if nums[i] in mapp and i - mapp[nums[i]] <=k: 
                return True
            mapp[nums[i]] = i
        
        return False