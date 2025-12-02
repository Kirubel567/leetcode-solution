class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        # +, D, C
        for i in range(len(operations)): 
            if operations[i] == "+": 
                second = int(stk[-1])
                first = 0
                if stk: 
                    first = int(stk[-2])

                Sum = first + second
                stk.append(Sum)

            elif operations[i] == "D": 
                result = stk[-1]
                stk.append(int(result)*2)
            elif operations[i] == "C": 
                stk.pop()
            else: 
                stk.append(int(operations[i]))
        
        return sum(stk)