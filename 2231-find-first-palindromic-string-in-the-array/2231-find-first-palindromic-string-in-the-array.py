class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)): 
            if words[i][::-1] == words[i]:
                return words[i] 
        else: 
            return ""