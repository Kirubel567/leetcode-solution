class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_counter = k
        
        left, max_len = 0, 0
        for i in range(len(nums)): 
            if nums[i] == 0: 
                zero_counter -=1
            while zero_counter < 0: 
                if nums[left] == 0: 
                    zero_counter += 1
                left += 1
        
            max_len = max(max_len, i - left +1)


        return max_len  