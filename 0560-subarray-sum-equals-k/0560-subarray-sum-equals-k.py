class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefStore = defaultdict(int)
        prefStore[0] = 1
        Sum, count = 0, 0
        for i in range(len(nums)): 
            Sum += nums[i]

            count += prefStore[Sum - k]

            prefStore[Sum] += 1
        
        return count 