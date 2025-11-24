class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            store = 0 
            for j in range(len(boxes)): 
                if boxes[j] != '0': 
                    store += abs(j-i)
            res.append(store)
        
        return res
