class Solution:
    def maxScore(self, s: str) -> int:
        #pre compute the postfix sum of 1's
        #iterate through the string and update the count 
        post_fix = [0]*len(s)
        accumulate = 0
        for i in range(len(s)-1, -1, -1):
            post_fix[i] = accumulate
            if s[i]=="1": 
                accumulate += 1
        
        #[0, 1, 1, 2, 3, 4]
        #[4, 3, 2, 1, 1, 0]
        zeros_before, res = 0, 0
        for i in range(len(s)): 
            if s[i] =="0": 
                zeros_before += 1
            
            res = max(res, post_fix[i] + zeros_before)
            if i == len(s) -2: 
                return res 

        return res 
            
