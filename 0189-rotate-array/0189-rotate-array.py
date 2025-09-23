class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)

        for i in range(len(nums)): 
            pos = (i + k) % len(nums)
            res[pos] = nums[i]
    
        for i in range(len(nums)): 
            nums[i] = res[i]

