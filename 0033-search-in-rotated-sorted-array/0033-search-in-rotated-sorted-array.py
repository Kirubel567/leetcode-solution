class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #dectect the largerst element of the division 
        pivot = 0

        while l < r: 
            mid = (l + r) // 2
            if nums[mid] > nums[r]: 
                l = mid + 1
            else: 
                r = mid
        
        pivot = l - 1 if l > 0 else len(nums) - 1

        
        if target <= nums[pivot] and target >= nums[0]: 
            left, right = 0, pivot 
        else: 
            left, right = pivot + 1, len(nums) - 1
    



        while left <= right: 
            middle = (right + left) // 2

            if nums[middle] == target: 
                return middle 
            elif nums[middle] < target: 
                left = middle + 1
            else: 
                right = middle - 1

        return -1 