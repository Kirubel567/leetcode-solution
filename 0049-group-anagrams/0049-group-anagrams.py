class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for s in strs: 
            Sorted = sorted(s)
            mapp[tuple(Sorted)].append(s)

        return list(mapp.values())