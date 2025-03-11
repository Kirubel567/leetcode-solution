class Solution:
    def isBalanced(self, num: str) -> bool:
        ListForm = list(num)
        evens = ListForm[::2]
        odds = ListForm[1::2]
        Sum = 0
        for even in evens:
            Sum += int(even)
        Sum2 = 0 
        for odd in odds:
            Sum2 += int(odd)
        return (Sum == Sum2)
        