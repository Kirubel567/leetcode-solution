class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        #sorting is the way to find if they could be rearranged into arthimetic sequence 
        #but after sorting you have to iterate through left[i] to right[i] 
        #any better way????
        tracker = 0
        res = []
        while tracker < len(l): 
            #get the subarray
            store = sorted(nums[l[tracker]:r[tracker]+1])

            #check if the subarray is in arthimetic sequence 
            compare = store[1] - store[0]
            checker = False
            for j in range(1, len(store)): 
                diff = store[j] - store[j-1]
                if diff != compare: 
                    res.append(False) 
                    break
            else: 
                res.append(True)
                
            tracker +=1
        return res 



