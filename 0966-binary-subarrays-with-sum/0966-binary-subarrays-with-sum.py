class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_sum = {0:1}
        count, Sum = 0, 0
        for i in range(len(nums)): 
            Sum += nums[i]

            count += pref_sum.get(Sum-goal, 0)
            pref_sum[Sum] = pref_sum.get(Sum, 0) + 1

        return count

