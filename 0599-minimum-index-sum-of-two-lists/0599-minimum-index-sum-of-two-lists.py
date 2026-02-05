class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        #use two dictionaries 
        dict1, dict2 = dict(), dict()

        for i, word in enumerate(list1): 
            dict1[word] = i
        for i, word in enumerate(list2): 
            dict2[word] = i
        
        print(dict1)
        print(dict2)
        res, ans = float('inf'), ''
        ansL = [] 
        for word in list1: 
            if word in list2: 
                Sum = dict1[word]+dict2[word]
                if res > Sum: 
                    res = Sum
                    ans = word
            
        ansL.append(ans)
        for word in list1: 
            if word in list2: 
                Sum = dict1[word] + dict2[word]
                if res == Sum and word not in ansL:
                    ansL.append(word) 
                    
        return ansL
