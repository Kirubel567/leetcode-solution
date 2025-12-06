class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        initial = sum(nums[:k])

        res = initial/k
        left = 0
        for r in range(k, len(nums)):
            initial += nums[r] - nums[left]
            current = initial/k

            res = max(res, current)
            left += 1

        return res 

