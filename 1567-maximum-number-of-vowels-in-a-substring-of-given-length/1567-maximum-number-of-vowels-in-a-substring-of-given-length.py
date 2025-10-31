class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #hold on to the first k items of the array
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(k): 
            if s[i] in vowels: 
                count +=1 
        
        tracker = 0
        currCount = count 
        for i in range(k, len(s)):  
            if s[tracker] in vowels: 
                currCount -= 1
            if s[i] in vowels: 
                currCount += 1
            tracker += 1
            count = max(count , currCount)
            
        return count 
