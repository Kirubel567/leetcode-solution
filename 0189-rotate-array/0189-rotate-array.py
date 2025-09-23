class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #first rotate the array 
        nums.reverse()
        k = k % len(nums)
        left, right = k,len(nums)-1
        print(nums)
        while left < right: 
            nums[right], nums[left] = nums[left], nums[right]
            right-=1
            left+= 1

        first, second = 0, k-1
        while first < second: 
            nums[first], nums[second] = nums[second], nums[first]
            first += 1
            second -= 1

          
        

