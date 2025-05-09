class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        ptr1 = 0
        ptr2 = 0

        while ptr1 < m and ptr2 < n: 
            if nums1[ptr1] <= nums2[ptr2]: 
                arr.append(nums1[ptr1])
                ptr1 += 1
            else: 
                arr.append(nums2[ptr2])
                ptr2 += 1

        while ptr1 < m: 
            arr.append(nums1[ptr1])
            ptr1 += 1 
        while ptr2 < n: 
            arr.append(nums2[ptr2])
            ptr2 += 1

        for i in range(m + n): 
            nums1[i] = arr[i]

                





        
        