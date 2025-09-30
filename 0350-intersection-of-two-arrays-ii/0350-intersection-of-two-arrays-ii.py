class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create a freq map to store the frequency of elements of nums1
        freq = Counter(nums1)

        #then iterate through nums2, if the element is in nums one add it to result and decrease the frequence of that element by one 
        res = []

        for i in range(len(nums2)): 
            if nums2[i] in freq and freq[nums2[i]] >0: 

                res.append(nums2[i])
                freq[nums2[i]] = freq.get(nums2[i], 0) -1
            
        return res 
