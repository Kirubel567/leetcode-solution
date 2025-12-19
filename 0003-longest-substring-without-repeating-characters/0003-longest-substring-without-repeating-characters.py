class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = defaultdict(int)
        left, count = 0, 0
        for i in range(len(s)): 
            mapp[s[i]]+=1
           
            while mapp[s[i]] > 1: 
                mapp[s[left]]-=1
                
                left += 1
            count = max(count, i - left +1)

        
        return count 

        
