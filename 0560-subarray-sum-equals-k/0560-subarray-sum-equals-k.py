class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, Sum, res = 0, 0, 0
        pref_sum = defaultdict(int)
        pref_sum[0] += 1

        for i in range(len(nums)): 
            Sum += nums[i]
            if Sum - k in pref_sum: 
                count += pref_sum[Sum - k]
            pref_sum[Sum] += 1
        return count 

        
