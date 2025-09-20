class Solution:
    def interpret(self, command: str) -> str:
        word = ""
        for i in range(len(command)): 
            if command[i] == "G": 
                word += command[i]
            elif command[i] == "(": 
                if i < len(command) - 1 and command[i + 1] == ")": 
                    word += "o"
                else: 
                    word += "al"
            
        return word
