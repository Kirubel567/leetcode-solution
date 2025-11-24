class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(list(s))

        def freq_sorter(ch):
            return (-freq[ch], ord(ch))

        to_sort_array = list(s)
        to_sort_array.sort(key=freq_sorter)

        return "".join(to_sort_array)
