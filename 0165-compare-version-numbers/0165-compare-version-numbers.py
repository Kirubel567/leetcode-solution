class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.split(".")
        lst2 = version2.split(".")

        v1, v2 = 0, 0 

        while v1 < len(lst1) and v2 <len(lst2): 
            if int(lst1[v1]) < int(lst2[v2]): 
                return -1
            elif int(lst1[v1]) > int(lst2[v2]): 
                return 1

            v1 += 1
            v2 += 1
        while v1 < len(lst1):
            if int(lst1[v1]) != 0:
                return 1
            v1 += 1

        # check remaining chunks in lst2
        while v2 < len(lst2):
            if int(lst2[v2]) != 0:
                return -1
            v2 += 1

        return 0
            
    



