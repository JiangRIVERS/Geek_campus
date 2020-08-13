# 在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。 
# 
#  一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成： 
# 
#  
#  相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角） 
#  C_1 位于 (0, 0)（即，值为 grid[0][0]） 
#  C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]） 
#  如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0） 
#  
# 
#  返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[0,1],[1,0]]
# 
# 输出：2
# 
#  
# 
#  示例 2： 
# 
#  输入：[[0,0,0],[1,1,0],[1,1,0]]
# 
# 输出：4
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    # BFS
        if grid[0][0] or grid[-1][-1]:
            return -1
        if len(grid) == 1:
            return 1
        n = len(grid)
        queue = {(0, 0)}
        visited = {(0, 0)}
        step = 1
        while queue:
            step += 1
            next_queue = set()
            for i in queue:
                j, k = i
                for _ in range(8):
                    x = j + dx[_]
                    y = k + dy[_]
                    if x == y == n - 1:
                        return step
                    if 0<= x < n and 0<= y < n and grid[x][y] != 1 and (x, y) not in visited:
                        next_queue.add((x, y))
                        visited.add((x, y))
            queue = next_queue
        return -1


# leetcode submit region end(Prohibit modification and deletion)
