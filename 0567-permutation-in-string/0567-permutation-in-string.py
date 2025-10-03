class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        n = len(s1)
        mapp = Counter(s1)
        check = Counter(s2[:n]) #use this inorder to remove the key value pair when the count is 0
        
        if mapp == check: 
            return True
        


        print(mapp)
        
        tracker = 0
        for i in range(n, len(s2)): 
            check[s2[tracker]] -= 1
            check[s2[i]] += 1

            tracker += 1

            print(check)
            if check == mapp: 
                return True

        return False 




