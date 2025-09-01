class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = float("inf")
        ans = 0
        for i in range(len(nums) - 1): 
            j = i + 1
            k = len(nums) - 1
            while j < k: 
                Sum = nums[i] + nums[k] + nums[j]
                currDiff = abs(Sum - target)
                if currDiff < minDiff: 
                    ans = Sum
                    minDiff = currDiff

                if Sum < target: 
                    j += 1
                elif Sum > target: 
                    k -= 1
                else: 
                    return Sum
                
        return ans

                