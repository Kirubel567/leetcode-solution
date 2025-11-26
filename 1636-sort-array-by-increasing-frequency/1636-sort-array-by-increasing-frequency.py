class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        def freq_sort(num):
            return (freq[num], -num)

        nums.sort(key=freq_sort)
        return nums