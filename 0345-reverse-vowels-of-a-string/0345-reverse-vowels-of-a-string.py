class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        arr = list(s)
        left, right = 0, len(arr)-1

        while left < right: 
            if arr[right] in vowels and s[left] in vowels: 
                arr[right], arr[left] = arr[left], arr[right]
                right -= 1
                left += 1

            if arr[right] not in vowels: 
                right -=1
            if arr[left] not in vowels: 
                left += 1
            
            
        
        return "".join(arr)