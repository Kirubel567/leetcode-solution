class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans, minValue = letters[0], float('inf')

        for i in range(len(letters)): 
            diff = ord(letters[i]) - ord(target)
            if diff > 0 and diff < minValue: 
                minValue = diff 
                ans = letters[i]
        
        return ans 