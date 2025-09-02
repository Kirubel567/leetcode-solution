class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        i = len(s) - 1

        while i >= 0:  
            string = ""

            while i >= 0 and s[i] == " ": 
                i -= 1
            while i >= 0 and s[i] != " ": 
                string += s[i]
                i -= 1
            if string: 
                lst.append(string[::-1])
            i -= 1
        
        print(lst)

        return " ".join(lst)
