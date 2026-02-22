class Solution:
    def binaryGap(self, n: int) -> int:
        Binary = bin(n)[2:]
        count, ans = 0, -float('inf')
        print(Binary)
        for i in range(len(Binary)): 
            count += 1
            if Binary[i] == "1": 
                ans = max(count, ans)
                count = 0
            
            
        return ans if Binary.count('1') > 1 else 0