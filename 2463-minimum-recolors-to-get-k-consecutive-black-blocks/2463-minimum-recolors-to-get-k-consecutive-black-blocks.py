class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = {"B": 0, "W": 0}
        starter, res = 0, float('inf')

        for i in range(k):
            count[blocks[i]] += 1
        res = min(res, count["W"])


        for i in range(k, len(blocks)): 
            count[blocks[i]] += 1
            count[blocks[starter]] -= 1
            starter+= 1

            res = min(res, count["W"])

        return res
            


