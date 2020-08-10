# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 回溯
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.num = 0
        self.i = len(grid)
        self.j = len(grid[0])

        def helper(i, j):
            if i not in range(0, self.i) or j not in range(0, self.j) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            helper(i, j + 1)
            helper(i, j - 1)
            helper(i + 1, j)
            helper(i - 1, j)

        for i in range(self.i):
            for j in range(self.j):
                if grid[i][j] == '1':
                    self.num += 1
                    helper(i, j)
        return self.num
'''
# 并查集
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
class UnionFind:
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.count = 0
        self.p = [-1] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.p[i * n + j] = i * n + j
                    self.count += 1

    def union(self, x, y):
        p1 = self._parent(x)
        p2 = self._parent(y)
        if p1 != p2:
            self.p[p2] = p1
            self.count -= 1

    def _parent(self, i):
        root = i
        while self.p[root] != root:
            root = self.p[root]
        while self.p[i] != i:
            x = i
            i = self.p[i]
            self.p[x] = root
        return root

    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)
        return uf.getCount()
'''
# leetcode submit region end(Prohibit modification and deletion)
