class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        Sum = sum(nums[left:k])
        max_avg = Sum
        for r in range(k, len(nums)):
            Sum -= nums[left]
            Sum += nums[r]
            
            max_avg = max(max_avg, Sum)
            left += 1

        return max_avg/k