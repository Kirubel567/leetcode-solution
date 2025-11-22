class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp1 = Counter(set(nums1))
        mapp2 = Counter(set(nums2))
        res = []
        for key in mapp1: 
            if key in mapp2: 
                res.extend([key] * mapp1[key])
        return res 