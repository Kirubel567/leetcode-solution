class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        Sqrt = num ** 0.5
        x = int(Sqrt)
        return x == Sqrt
