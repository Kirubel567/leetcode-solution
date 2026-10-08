class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        for i in range(len(strs[0])): 
            for j in range(len(strs)): 
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]: 
                    return ans
            ans += strs[0][i]
        return ans
        