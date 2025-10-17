class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)//4
        left, ans = 0, float("inf")
        count = defaultdict(int)
        for letter in s: 
            count[letter] += 1

        if max(count.values()) == n: 
            return 0

        for right in range(len(s)): 
            count[s[right]] -=1

            while left <= right and max(count.values()) <= n: 
                ans = min(ans, right - left +1)
                count[s[left]] += 1
                left += 1

        return ans 