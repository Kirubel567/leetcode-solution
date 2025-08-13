class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for s in strs: 
            count = [0] * 26

            for ch in s: 
                count[ord(ch) - ord("a")] += 1 
            mapp[tuple(count)].append(s)

        return list(mapp.values())


