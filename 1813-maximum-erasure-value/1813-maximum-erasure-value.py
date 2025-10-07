class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)
        tracker, Sum, res = 0,0, 0

        for i in range(len(nums)):
            if count[nums[i]] == 0: 
                count[nums[i]] += 1 
                Sum += nums[i]
            else: 
                while tracker < i: 
                    count[nums[tracker]] -= 1
                    Sum -= nums[tracker]
            
                    if nums[tracker] == nums[i]: 
                        tracker += 1
                        break
                    tracker += 1
                    
                count[nums[i]] += 1
                Sum += nums[i]
        
            res = max(Sum, res)
               
        return res
                
            


