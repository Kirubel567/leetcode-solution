class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums2)
        mapp = defaultdict(int)
        stk = []
        for i in range(len(nums2)-1, -1,-1): 
            while stk and nums2[i] >= stk[-1]: 
                stk.pop()
            
            if stk: 
                ans[i] = stk[-1]
            mapp[nums2[i]] = ans[i]
            
            stk.append(nums2[i])
        
        for i in range(len(nums1)): 
            nums1[i] = mapp[nums1[i]]
        
        return nums1
