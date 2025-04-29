class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        Index = []
        nums.sort()

        for i in range(len(nums)): 
            if nums[i] == target: 
                Index.append(i)
        return Index
        
        


