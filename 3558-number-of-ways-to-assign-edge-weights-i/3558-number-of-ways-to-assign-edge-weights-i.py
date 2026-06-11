class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10**9 + 7

        tree = defaultdict(list)

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(root : int, prev : int = -1) -> int:
            if not tree[root]: return 0

            maxDepth = depth = 0
            for child in tree[root]:
                if child != prev:
                    depth = 1 + dfs(child, root)
                    maxDepth = max(maxDepth, depth)

            return maxDepth

        maxDepth = dfs(1)

        return pow(2, maxDepth - 1, mod)