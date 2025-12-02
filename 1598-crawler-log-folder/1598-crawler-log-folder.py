class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #we could just start a variable counter, then if moving forward +1, staying at a folder +0, and moving back one -1
        #then return count
        count = 0
        for i in range(len(logs)): 
            if logs[i] != "./": 
                if logs[i] == "../": 
                    if count != 0: 
                        count -=1
                else: 
                    count +=1 
        
        return count if count >=0 else 0
