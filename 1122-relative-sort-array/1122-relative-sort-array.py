class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        answer = []
        for i in range(len(arr2)): 
            for j in range(freq[arr2[i]]): 
                answer.append(arr2[i])
        sorter = []
        for i in range(len(arr1)): 
            if arr1[i] not in arr2: 
                sorter.append(arr1[i])

        return answer + sorted(sorter)
