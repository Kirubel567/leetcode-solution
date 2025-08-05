class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        odd = 0
        for i in range(len(nums)): 
            if i % 2 == 0: 
                odd = nums[i]
            else: 
                arr.append(nums[i])
                arr.append(odd)

        return arr