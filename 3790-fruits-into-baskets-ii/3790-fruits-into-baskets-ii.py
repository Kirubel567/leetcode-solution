class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        counter = 0
        holder={}

        
        for i in range(n): 
            for j in range(n): 
                if fruits[i] <= baskets[j]: 
                    baskets[j] = -1
                    break 
            else: 
                counter += 1

        return counter