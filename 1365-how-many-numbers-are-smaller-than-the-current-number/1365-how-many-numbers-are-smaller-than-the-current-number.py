class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        idxHolder = defaultdict(int)
        sor = sorted(nums)
        for i in range(len(sor)): 
            if sor[i] not in idxHolder:
                idxHolder[sor[i]] = i


        res = []
        for i in range(len(nums)): 
            res.append(idxHolder[nums[i]])

        return res