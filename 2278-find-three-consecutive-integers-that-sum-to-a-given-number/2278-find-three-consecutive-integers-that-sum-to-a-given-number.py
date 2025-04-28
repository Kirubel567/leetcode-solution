class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr = []
        x = 0

        x = num // 3

        if x + (x - 1) + (x + 1) == num: 
            arr.append(x - 1)
            arr.append(x)
            arr.append(x + 1)

        return arr

        
        