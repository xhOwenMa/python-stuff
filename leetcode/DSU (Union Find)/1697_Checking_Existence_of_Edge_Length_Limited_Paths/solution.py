# will use union find:
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def combine(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]

    def are_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        queries_count = len(queries)
        answer = [False] * queries_count
        
        # Sort all edges in increasing order of their edge weights.
        sorted_edges = sorted(edgeList, key=lambda x: x[2])
        # Sort all queries in increasing order of the limit of edge allowed.
        #   enumerate(queries) create (index, query) pair, therefore this helps us to keep track of the original index where a specific query is passed in
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][2])

        i = 0 # this does need to be resetted for each query because we are doing everything in ascending order based on edge distances and query limits, this way we do not need to reconsider edges for every query
        for query_index, (p, q, limit) in sorted_queries:
            while i < len(edgeList) and sorted_edges[i][2] < limit:
                uf.combine(sorted_edges[i][0], sorted_edges[i][1])
                i += 1

            answer[query_index] = uf.are_connected(p, q)
        
        return answer