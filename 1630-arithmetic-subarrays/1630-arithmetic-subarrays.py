class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for left, right in zip(l, r): 
            store = sorted(nums[left:right+1])
            diff = store[1]-store[0]
            res.append(all(store[i]-store[i-1] == diff for i in range(1, len(store))))
        
        return res 