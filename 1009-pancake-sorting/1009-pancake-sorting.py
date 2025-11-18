class Solution:
    def pancakeSort(self, arr):
        result, n = [], len(arr)
        for i in range(n,0,-1):
            pl = arr.index(i)
            if pl == i-1: continue
            if pl != 0:
                result.append(pl+1)
                arr[:pl+1] = arr[:pl+1][::-1]
            result.append(i)
            arr[:i] = arr[:i][::-1]
            
        return result