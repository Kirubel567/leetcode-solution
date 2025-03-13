class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(1000000)
        Num = 0 
        for i in num:
            Num = Num * 10 + i
        Sum = Num + k 
        StringList = str(Sum)
        List = []
        for i in StringList:
            List = List + [int(i)]
        return List
