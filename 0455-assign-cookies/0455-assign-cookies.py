class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #function : maximize the content of each child 
        #variables: the candies with their sizes
        # constraint : 1 for each child
        
        #sort both the children and the candies 
        g.sort()
        s.sort()

        content = 0
        gp, sp = 0, 0
        while gp < len(g) and sp < len(s): 
            if g[gp] <= s[sp]: 
                content += 1
                gp += 1
            sp += 1


        return content 
