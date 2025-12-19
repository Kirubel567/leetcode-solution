class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        Sum = sum(nums[left:k])
        max_avg = Sum/k
        for r in range(k, len(nums)):
            Sum -= nums[left]
            Sum += nums[r]
            
            max_avg = max(max_avg, Sum/k)
            left += 1

        return max_avg