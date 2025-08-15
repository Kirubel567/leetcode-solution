class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = Counter(nums)
        arr1 = list(mapp.values())
        arr1.sort()
        arr = [0] * len(arr1)

        for key in mapp: 
            idx = arr1.index(mapp[key])
            arr1[idx] = -1
            arr[idx] = key

        return arr[::-1][:k]

       