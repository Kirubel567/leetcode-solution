class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #define a hashmap to store the frequency of the elements in arr1
        freq = {}

        for i in range(len(arr1)): 
            freq[arr1[i]] = freq.get(arr1[i], 0) +1
        
        #iterate through the second array and map them in a new arr
        res = []

        for j in range(len(arr2)): 
            
            count = freq[arr2[j]]
            for i in range(count): 
                res.append(arr2[j])
        
        rest = []
        for key, value in freq.items(): 
            if key not in arr2: 
                count = value
                if count > 0: 
                    rest.extend([key] * count)
        
        
        res.extend(sorted(rest))

        
        return res 
