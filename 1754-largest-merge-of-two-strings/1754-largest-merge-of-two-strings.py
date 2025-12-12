class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        one, two, merged = 0, 0, ""

        while one < len(word1) and two < len(word2): 
            if word1[one:] >= word2[two:]: 
                merged+= word1[one]
                one+= 1
            else: 
                merged+=word2[two]
                two += 1
         
        merged += word1[one:]
        merged += word2[two:]

        return merged 