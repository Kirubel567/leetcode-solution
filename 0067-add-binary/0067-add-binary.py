class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A, B = int(a, 2), int(b, 2) 
        return bin(A + B)[2:]


        