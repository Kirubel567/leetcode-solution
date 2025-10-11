class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = defaultdict(int)
        pref_sum[0]=1
        count, Sum = 0, 0

        for i in range(len(nums)): 
            Sum += nums[i]
            remainder = Sum % k

            count += pref_sum[remainder]
            pref_sum[remainder] += 1
        
        return count

