# this is the DFS method I'm able to come up with, runs much slower than the union-find algorithm

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)
        groups = 0
        visited = [False] * n 
        # then we can use DFS to connect all the similar strings together
        for i in range(n):
            if visited[i]:
                continue
            groups += 1
            visited[i] = True
            self.dfs(i, strs, visited)

        return groups


    # first: observe that two strings x and y are similar if:
    #   1, they differ in 2 places so that we can swap them
    #   2, they are the same (differ in 0 places)
    def isSimilar(self, s1, s2) -> bool:
        diff = 0
        for c in range(len(s1)):
            if s1[c] != s2[c]:
                diff += 1

        return diff == 2 or diff == 0


    def dfs(self, i: int, strs: List[str], visited: List[bool]) -> None:
        for j in range(len(strs)):
            if self.isSimilar(strs[i], strs[j]):
                if visited[j]:
                    continue
                visited[j] = True
                self.dfs(j, strs, visited)


# below is the union-find algorithm
        
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.count -= 1

        return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            if s1 == s2:
                return True

            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False

            return diff == 2

        n = len(strs)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    uf.union(i, j)

        return uf.count
      
