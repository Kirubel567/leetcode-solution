class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapp = {}
        char = 'a'
        for i in range(len(key)): 
            if key[i] != ' ' and key[i] not in mapp:
                mapp[key[i]] = char
                char = chr(ord(char) + 1)
        result = ""
        for j in range(len(message)): 
            if message[j] != ' ': 
                result += mapp[message[j]]
            else: 
                result += ' '
            
        return result

             

